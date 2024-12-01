from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.groups import GroupRepository
from src.schemas import GroupModel, GroupResponse


class GroupService:
    def __init__(self, db: AsyncSession):
        self.repository = GroupRepository(db)

    async def create_group(self, body: GroupModel):
        return await self.repository.create_group(body)

    async def get_groups(self, skip: int, limit: int):
        return await self.repository.get_groups(skip, limit)

    async def get_group(self, group_id: int):
        return await self.repository.get_group_by_id(group_id)

    async def update_group(self, group_id: int, body: GroupModel):
        return await self.repository.update_group(group_id, body)

    async def remove_group(self, group_id: int):
        return await self.repository.remove_group(group_id)
