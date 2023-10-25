from fastapi import APIRouter

router =APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

# https://himalayas.app/jobs/api?limit=100&offset=10
@router.get("/test")
def test():
    return "test"