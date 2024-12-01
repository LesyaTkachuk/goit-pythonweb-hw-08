from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.schemas import GroupModel, GroupResponse
from src.services.groups import GroupService

router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("/", response_model=List[GroupResponse])
async def read_groups(
    skip: int = 0, limit: int = 50, db: AsyncSession = Depends(get_db)
):
    group_service = GroupService(db)
    groups = await group_service.get_groups(skip, limit)
    return groups


@router.get("/{group_id", response_model=GroupResponse)
async def read_group(group_id: int, db: AsyncSession = Depends(get_db)):
    group_service = GroupService(db)
    group = await group_service.get_group(group_id)

    if group is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Group not found"
        )

    return group


@router.post("/", response_model=GroupResponse, status_code=status.HTTP_201_CREATED)
async def create_group(body: GroupModel, db: AsyncSession = Depends(get_db)):
    group_service = GroupService(db)
    return await group_service.create_group(body)


@router.put("/{group_id}", response_model=GroupResponse)
async def update_group(
    group_id: int, body: GroupModel, db: AsyncSession = Depends(get_db)
):
    group_service = GroupService(db)
    group = await group_service.update_group(group_id, body)
    if group is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Group not found"
        )
    return group


@router.delete("/{group_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_group(group_id: int, db: AsyncSession = Depends(get_db)):
    group_service = GroupService(db)
    return await group_service.remove_group(group_id)


# @router.delete("/{group_id}", response_model=GroupResponse)
# async def remove_group(group_id: int, db: AsyncSession = Depends(get_db)):
#     group_service = GroupService(db)
#     group = await group_service.remove_group(group_id)
#     if group is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Group not found"
#         )
#     return group
