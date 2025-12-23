# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class BCD(Segment):
    """
    BCD - Beginning Credit/Debit Adjustment
    
    Description:
        To transmit identifying dates and numbers for the transaction set and indicate the monetary value to the receiver of the transaction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BCD/
    """
    _id: Literal["BCD"] = id_element(name="BCD")

    Date: X12DT = element(
        name="BCD01",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    CreditDebitAdjustmentNumber: X12AN = element(
        name="BCD02",
        description="Credit/Debit Adjustment Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    TransactionHandlingCode: X12ID = element(
        name="BCD03",
        description="Transaction Handling Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Amount: X12Nn = element(
        name="BCD04",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    CreditDebitFlagCode: X12ID = element(
        name="BCD05",
        description="Credit/Debit Flag Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date2: Optional[X12DT] = element(
        name="BCD06",
        description="Date",
        min_length=8,
        max_length=8,
    )

    InvoiceNumber: Optional[X12AN] = element(
        name="BCD07",
        description="Invoice Number",
        min_length=1,
        max_length=22,
    )

    VendorOrderNumber: Optional[X12AN] = element(
        name="BCD08",
        description="Vendor Order Number",
        min_length=1,
        max_length=22,
    )

    Date3: Optional[X12DT] = element(
        name="BCD09",
        description="Date",
        min_length=8,
        max_length=8,
    )

    PurchaseOrderNumber: Optional[X12AN] = element(
        name="BCD10",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="BCD11",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BCD12",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="BCD13",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BCD14",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ActionCode: Optional[X12ID] = element(
        name="BCD15",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
