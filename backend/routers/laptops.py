from fastapi import APIRouter, HTTPException, Query

from crud import (
    get_all_laptops,
    get_laptop_by_id,
    create_laptop,
    update_laptop,
    delete_laptop,
    search_laptops,
)

from schemas import Laptop

router = APIRouter()


@router.get("/laptops")
def get_laptops():
    return get_all_laptops()

@router.get("/laptops/search")
def search_laptops_route(q: str = Query(...)):
    return search_laptops(q)

@router.get("/laptops/{laptop_id}")
def get_single_laptop(laptop_id: int):

    laptop = get_laptop_by_id(laptop_id)

    if laptop is None:
        raise HTTPException(
            status_code=404,
            detail="Laptop not found",
        )

    return dict(laptop)


@router.post("/laptops")
def add_laptop(laptop: Laptop):

    create_laptop(laptop)

    return {
        "message": "Laptop added successfully"
    }


@router.put("/laptops/{laptop_id}")
def update_laptop_route(laptop_id: int, laptop: Laptop):

    rows_updated = update_laptop(laptop_id, laptop)

    if rows_updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Laptop not found",
        )

    return {
        "message": "Laptop updated successfully"
    }


@router.delete("/laptops/{laptop_id}")
def delete_laptop_route(laptop_id: int):

    rows_deleted = delete_laptop(laptop_id)

    if rows_deleted == 0:
        raise HTTPException(
            status_code=404,
            detail="Laptop not found",
        )

    return {
        "message": "Laptop deleted successfully"
    }

