from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Group
from src.schemas import GroupModel, GroupResponse


class GroupRepository:
    def __init__(self, session: AsyncSession):
        self.db = session

    async def get_groups(self, skip: int, limit: int) -> List[Group]:
        stmt = select(Group).offset(skip).limit(limit)
        groups = await self.db.execute(stmt)
        return groups.scalars().all()

    async def get_group_by_id(self, group_id: int) -> Group | None:
        stmt = select(Group).filter_by(id=group_id)
        group = await self.db.execute(stmt)
        return group.scalar_one_or_none()

    async def create_group(self, body: GroupModel) -> Group:
        group = Group(**body.model_dump(exclude_unset=True))
        self.db.add(group)
        await self.db.commit()
        await self.db.refresh(group)
        return group

    async def update_group(self, group_id: int, body: GroupModel) -> Group | None:
        group = await self.get_group_by_id(group_id)
        if group:
            group.name = body.name
            await self.db.commit()
            await self.db.refresh(group)

        return group

    async def remove_group(self, group_id: int) -> Group | None:
        group = await self.get_group_by_id(group_id)
        if group:
            await self.db.delete(group)
            await self.db.commit()
        return group

    async def get_groups_by_ids(self, group_ids: List[int]) -> List[Group]:
        stmt = select(Group).where(Group.id.in_(group_ids))
        result = await self.db.execute(stmt)
        return result.scalars().all()
