from ninja import Router
from .chicken import router as chicken_router
from .dry_fruits import router as dryfruits_router
from .sweets import router as sweets_router

# Create main products router
router = Router()

# Add sub-routers
router.add_router("", chicken_router)
router.add_router("", dryfruits_router)
router.add_router("", sweets_router)

__all__ = ['router']
