from sanic import Blueprint
from .services import ApartmentService


bp = Blueprint("apartment")


@bp.get("/apartments")
async def search_apartments(_request):
    """
    Return a list of apartments matching query.
    """
    return ApartmentService.search()


@bp.get("/apartments/<uid:string>")
def get_apartment_details(_request, uid):
    """
    Return details of a single apartment given by its uid.
    """
    return ApartmentService.get_details(uid)


@bp.post("/apartments")
def create_apartment(request):
    """
    Create apartment from JSON body's data.
    """
    return ApartmentService.create(request.json)


@bp.put("/apartments/<uid:string>")
def update_apartment(request, uid):
    """
    Return a list of apartments matching query.
    """
    return ApartmentService.update(uid, request.json)


@bp.delete("/apartments/<uid:string>")
def delete_apartment(_request, uid):
    return ApartmentService.delete(uid)
