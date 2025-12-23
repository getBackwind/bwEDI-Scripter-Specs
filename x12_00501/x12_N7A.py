# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class N7A(Segment):
    """
    N7A - Accessorial Equipment Details
    
    Description:
        To identify the accessorial equipment required to load or unload product
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/N7A/
    """
    _id: Literal["N7A"] = id_element(name="N7A")

    LoadOrDeviceCode: Optional[X12ID] = element(
        name="N7A01",
        description="Load or Device Code",
        min_length=2,
        max_length=2,
    )

    Length: Optional[X12R] = element(
        name="N7A02",
        description="Length",
        min_length=1,
        max_length=8,
    )

    Diameter: Optional[X12R] = element(
        name="N7A03",
        description="Diameter",
        min_length=1,
        max_length=2,
    )

    HoseTypeCode: Optional[X12ID] = element(
        name="N7A04",
        description="Hose Type Code",
        min_length=3,
        max_length=3,
    )

    Diameter2: Optional[X12R] = element(
        name="N7A05",
        description="Diameter",
        min_length=1,
        max_length=2,
    )

    Diameter3: Optional[X12R] = element(
        name="N7A06",
        description="Diameter",
        min_length=1,
        max_length=2,
    )

    InletOrOutletMaterialTypeCode: Optional[X12ID] = element(
        name="N7A07",
        description="Inlet or Outlet Material Type Code",
        min_length=2,
        max_length=2,
    )

    InletOrOutletFittingTypeCode: Optional[X12ID] = element(
        name="N7A08",
        description="Inlet or Outlet Fitting Type Code",
        min_length=2,
        max_length=2,
    )

    MiscellaneousEquipmentCode: Optional[X12ID] = element(
        name="N7A09",
        description="Miscellaneous Equipment Code",
        min_length=2,
        max_length=2,
    )
