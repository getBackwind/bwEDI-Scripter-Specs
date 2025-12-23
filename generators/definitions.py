from typing import Optional, Literal
from .segment import Segment, element, id_element, null_element


class BIG(Segment):
    _id: Literal["BIG"] = id_element(name="BIG")

    InvoiceDate: Optional[str] = element(
        name="BIG01",
        description="Invoice Date",
        min_length=8,
        max_length=8,
    )

    InvoiceID: Optional[str] = element(
        name="BIG02",
        description="Invoice Number",
        min_length=1,
        max_length=22,
    )

    PurchaseOrderDate: Optional[str] = element(
        name="BIG03",
        description="Purchase Order Date",
        min_length=8,
        max_length=8,
    )

    PurchaseOrderID: Optional[str] = element(
        name="BIG04",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    BIG05: Optional[str] = null_element(name="BIG05")

    BIG06: Optional[str] = null_element(name="BIG06")

    TransactionType: Optional[str] = element(
        name="BIG07",
        description="Transaction Type",
        min_length=2,
        max_length=2,
    )


class ISA(Segment):
    _id: Literal["ISA"] = id_element(name="ISA")

    AuthorizationQualifier: str = element(
        name="ISA01",
        description="Authorization Information Qualifier",
        min_length=2,
        max_length=2,
    )

    Authorization: str = element(
        name="ISA02",
        description="Authorization Information",
        min_length=10,
        max_length=10,
    )

    SecurityQualifier: str = element(
        name="ISA03",
        description="Security Information Qualifier",
        min_length=2,
        max_length=2,
    )

    Security: str = element(
        name="ISA04",
        description="Security Information",
        min_length=10,
        max_length=10,
    )

    SenderIdQualifier: str = element(
        name="ISA05",
        description="Sender ID Qualifier",
        min_length=2,
        max_length=2,
    )

    SenderID: str = element(
        name="ISA06",
        description="Interchange Sender ID",
        min_length=15,
        max_length=15,
    )

    ReceiverIdQualifier: str = element(
        name="ISA07",
        description="Receiver ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ReceiverID: str = element(
        name="ISA08",
        description="Interchange Receiver ID",
        min_length=15,
        max_length=15,
    )

    Date: str = element(
        name="ISA09",
        description="Interchange Date",
        min_length=6,
        max_length=6,
    )

    Time: str = element(
        name="ISA10",
        description="Interchange Time",
        min_length=4,
        max_length=4,
    )

    ControlStandardID: str = element(
        name="ISA11",
        description="Control Standard ID",
        min_length=1,
        max_length=1,
    )

    ControlVersionNumber: str = element(
        name="ISA12",
        description="Interchange Control Version Number",
        min_length=5,
        max_length=5,
    )

    ControlNumber: str = element(
        name="ISA13",
        description="Interchange Control Number",
        min_length=9,
        max_length=9,
    )

    Acknowledgment: str = element(
        name="ISA14",
        description="Acknowledgment Requested",
        min_length=1,
        max_length=1,
    )

    UsageIndicator: str = element(
        name="ISA15",
        description="Usage Indicator",
        min_length=1,
        max_length=1,
    )

    ComponentElementSeparator: str = element(
        name="ISA16",
        description="Component Element Separator",
        min_length=1,
        max_length=1,
    )


class SE(Segment):
    _id: Literal["SE"] = id_element(name="SE")

    SegmentsCount: Optional[str] = element(
        name="SE01",
        description="Total number of segments included in a transaction set",
        min_length=1,
        max_length=10,
    )

    TransactionSetID: Optional[str] = element(
        name="SE02",
        description="Transaction Set Control Number",
        min_length=4,
        max_length=9,
    )


class ST(Segment):
    _id: Literal["ST"] = id_element(name="ST")

    TransactionSetIdCode: str = element(
        name="ST01",
        description="Transaction Set type Identifier Code",
        min_length=3,
        max_length=3,
    )

    TransactionSetID: str = element(
        name="ST02",
        description="Transaction Set Control Number",
        min_length=4,
        max_length=9,
    )

"""
    ConventionID: str = element(
        name="ST03",
        description="Implementation Convention Reference",
        min_length=1,
        max_length=35,
        default=""
    )
"""


class GE(Segment):
    _id: Literal["GE"] = id_element(name="GE")

    TransactionSetCount: str = element(
        name="GE01",
        description="Number of Transaction Sets Included",
        min_length=1,
        max_length=6,
    )

    GroupID: str = element(
        name="GE02",
        description="Group Control Number",
        min_length=1,
        max_length=9,
    )


class GS(Segment):
    _id: Literal["GS"] = id_element(name="GS")

    FunctionalIdCode: str = element(
        name="GS01",
        description="Functional Identifier Code",
        min_length=2,
        max_length=2,
    )

    SenderID: str = element(
        name="GS02",
        description="Application Sender’s Code",
        min_length=2,
        max_length=15,
    )

    ReceiverID: str = element(
        name="GS03",
        description="Application Receiver’s Code",
        min_length=2,
        max_length=15,
    )

    Date: str = element(
        name="GS04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: str = element(
        name="GS05",
        description="Time",
        min_length=4,
        max_length=8,
    )

    GroupID: str = element(
        name="GS06",
        description="Group Control Number",
        min_length=1,
        max_length=9,
    )

    AgencyCode: str = element(
        name="GS07",
        description="Responsible Agency Code",
        min_length=1,
        max_length=2,
    )

    VersionID: str = element(
        name="GS08",
        description="Version / Release / Industry Identifier Code",
        min_length=1,
        max_length=12,
    )


class IEA(Segment):
    _id: Literal["IEA"] = id_element(name="IEA")

    GroupCount: str = element(
        name="IEA01",
        description="Number of Included Functional Groups",
        min_length=1,
        max_length=5,
    )

    InterchangeID: str = element(
        name="IEA02",
        description="Interchange Control Number",
        min_length=9,
        max_length=9,
    )


class BEG(Segment):
    _id: Literal["BEG"] = id_element(name="BEG")

    PurposeCode: Optional[str] = element(
        name="BEG01",
        description="Code identifying purpose of transaction set",
        min_length=2,
        max_length=2,
    )

    TypeCode: Optional[str] = element(
        name="BEG02",
        description="Code specifying the type of Purchase Order",
        min_length=2,
        max_length=2,
    )

    PurchaseOrderNumber: Optional[str] = element(
        name="BEG03",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    BEG04: Optional[str] = null_element(name="BEG04")

    Date: Optional[str] = element(
        name="BEG05",
        description="Date expressed as CCYYMMDD where CC represents the first two digits of the calendar year",
        min_length=8,
        max_length=8,
    )

    ContractNumber: Optional[str] = element(
        name="BEG06",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )


class CUR(Segment):
    _id: Literal["CUR"] = id_element(name="CUR")

    EntityIdentifierCode: Optional[str] = element(
        name="CUR01",
        description="Entity Identifier Code. SE = selling party",
        min_length=2,
        max_length=3,
    )

    CurrencyCode: Optional[str] = element(
        name="CUR02",
        description="Code (Standard ISO) for country in whose currency the charges are specified",
        min_length=3,
        max_length=3,
    )


class PID(Segment):
    _id: Literal["PID"] = id_element(name="PID")

    DescriptionType: str = element(
        name="PID01",
        description="Item Description Type",
        min_length=1,
        max_length=2,
    )

    CharCode: Optional[str] = element(
        name="PID02",
        description="Prod/Proc Char Code",
        min_length=2,
        max_length=3,
    )

    PID03: Optional[str] = null_element(name="PID03")

    PID04: Optional[str] = null_element(name="PID04")

    Description: Optional[str] = element(
        name="PID05",
        description="Description",
        min_length=1,
        max_length=80,
    )


class CN1(Segment):
    _id: Literal["CN1"] = id_element(name="CN1")

    ContractTypeCode: Optional[str] = element(
        name="CN101",
        description="Contract Type Code",
        min_length=2,
        max_length=2,
    )

    Amount: Optional[str] = element(
        name="CN102",
        description="Monetary Amount",
        min_length=1,
        max_length=15,
    )

    Percent: Optional[str] = element(
        name="CN103",
        description="Percent",
        min_length=1,
        max_length=6,
    )

    ReferenceID: Optional[str] = element(
        name="CN104",
        description="Reference Number",
        min_length=1,
        max_length=30,
    )

    TermsDiscountID: Optional[str] = element(
        name="CN105",
        description="Terms Discount Number",
        min_length=1,
        max_length=6,
    )

    VersionID: Optional[str] = element(
        name="CN106",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )


class DTM(Segment):
    _id: Literal["DTM"] = id_element(name="DTM")

    DateTimeQualifier: Optional[str] = element(
        name="DTM01",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[str] = element(
        name="DTM02",
        description="Date expressed as CCYYMMDD",
        min_length=8,
        max_length=8,
    )

    Time: Optional[str] = element(
        name="DTM03",
        description="Time expressed in 24-hour clock time as follows: HHMM, or HHMMSS, or HHMMSSD, or HHMMSSDD",
        min_length=4,
        max_length=8,
    )


class IT1(Segment):
    _id: Literal["IT1"] = id_element(name="IT1")

    LineID: Optional[str] = element(
        name="IT101",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    Quantity: Optional[str] = element(
        name="IT102",
        description="Quantity Invoiced",
        min_length=1,
        max_length=10,
    )

    UOM: Optional[str] = element(
        name="IT103",
        description="Unit of Measure Code",
        min_length=2,
        max_length=2,
    )

    UnitPrice: Optional[str] = element(
        name="IT104",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    BasisOfUnitPrice: Optional[str] = element(
        name="IT105",
        description="Unit Price",
        min_length=2,
        max_length=2,
        )

    ItemIdQualifier: Optional[str] = element(
        name="IT106",
        description="Product/Serv ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID: Optional[str] = element(
        name="IT107",
        description="Product/Serv ID",
        min_length=1,
        max_length=48,
    )


class IT3(Segment):
    _id: Literal["IT3"] = id_element(name="IT3")

    UnitsShipped: Optional[str] = element(
        name="IT301",
        description="Numeric value of units shipped in manufacturer's shipping units for a line item or transaction set",
        min_length=1,
        max_length=10,
    )

    UnitCode: Optional[str] = element(
        name="IT302",
        description="Code specifying the units in which a value is being expressed, or manner in which a measurement has been taken",
        min_length=2,
        max_length=2,
    )


class BIA(Segment):
    _id: Literal["BIA"] = id_element(name="BIA")

    PurposeCode: Optional[str] = element(
        name="BIA01",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    ReportTypeCode: Optional[str] = element(
        name="BIA02",
        description="Code indicating the title or contents of a document, report or supporting item",
        min_length=2,
        max_length=2,
    )

    RefID: Optional[str] = element(
        name="BIA03",
        description="Reference information as defined for a particular Transaction Set or as "
                    "specified by the Reference Identification Qualifier",
        min_length=1,
        max_length=30,
    )

    Date: Optional[str] = element(
        name="BIA04",
        description="Date expressed as CCYYMMDD",
        min_length=8,
        max_length=8,
    )

    Time: Optional[str] = element(
        name="BIA05",
        description="Time expressed in 24-hour clock time as follows: HHMM, or HHMMSS, or HHMMSSD, or HHMMSSDD,",
        min_length=4,
        max_length=8,
    )


class QTY(Segment):
    _id: Literal["QTY"] = id_element(name="QTY")

    QuantityQualifier: Optional[str] = element(
        name="QTY01",
        description="Code specifying the type of quantity",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[str] = element(
        name="QTY02",
        description="Numeric value of quantity",
        min_length=1,
        max_length=15,
    )

    UOM: Optional[str] = element(
        name="QTY03",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )



class TXI(Segment):
    _id: Literal["TXI"] = id_element(name="TXI")

    TaxType: Optional[str] = element(
        name="TXI01",
        description="Tax Type Code",
        min_length=2,
        max_length=2,
    )

    Amount: Optional[str] = element(
        name="TXI02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Percent: Optional[str] = element(
        name="TXI03",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    JurisdictionQualifier: Optional[str] = element(
        name="TXI04",
        description="Jurisdiction Qualifier",
        min_length=2,
        max_length=2,
    )

    JurisdictionCode: Optional[str] = element(
        name="TXI05",
        description="Jurisdiction Code",
        min_length=1,
        max_length=10,
    )

    TXI06: Optional[str] = null_element(name="TXI06")

    TXI07: Optional[str] = null_element(name="TXI07")

    TXI08: Optional[str] = null_element(name="TXI08")

    RegistrationNumber: Optional[str] = element(
        name="TXI09",
        description="Registration Number",
        min_length=1,
        max_length=20,
    )

    Description: Optional[str] = element(
        name="TXI10",
        description="Description",
        min_length=1,
        max_length=20,
    )


class ISS(Segment):
    _id: Literal["ISS"] = id_element(name="ISS")

    UnitsShipped: Optional[str] = element(
        name="ISS01",
        description="Numeric value of units shipped in manufacturer's shipping units for a line item or transaction set",
        min_length=1,
        max_length=10,
    )

    UomCode: Optional[str] = element(
        name="ISS02",
        description="Code specifying the units in which a value is being expressed, or manner in which a measurement has been taken",
        min_length=2,
        max_length=2,
    )

    Weight: Optional[str] = element(
        name="ISS03",
        description="Numeric value of weight",
        min_length=1,
        max_length=10,
    )

    WeightUomCode: Optional[str] = element(
        name="ISS04",
        description="Code specifying the units in which a value is being expressed, or manner in which a measurement has been taken",
        min_length=2,
        max_length=2,
    )


class YNQ(Segment):
    _id: Literal["YNQ"] = id_element(name="YNQ")

    ConditionIndicator: Optional[str] = element(
        name="YNQ01",
        description="The loop ID number given on the transaction set diagram is the value for this data element in segments LS and LE",
        min_length=2,
        max_length=3,
    )

    YesNoValue: Optional[str] = element(
        name="YNQ02",
        description="Code indicating a Yes or No condition or response. Y, or N",
        min_length=1,
        max_length=1,
    )


class LS(Segment):
    _id: Literal["LS"] = id_element(name="LS")

    LoopID: Optional[str] = element(
        name="LS01",
        description="The loop ID number given on the transaction set diagram is the value for this data element in segments LS and LE",
        min_length=2,
        max_length=3,
    )


class LE(Segment):
    _id: Literal["LE"] = id_element(name="LE")

    LoopID: Optional[str] = element(
        name="LE01",
        description="The loop ID number given on the transaction set diagram is the value for this data element in segments LS and LE",
        min_length=2,
        max_length=3,
    )


class REF(Segment):
    _id: Literal["REF"] = id_element(name="REF")

    Qualifier: Optional[str] = element(
        name="REF01",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ID: Optional[str] = element(
        name="REF02",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Description: Optional[str] = element(
        name="REF03",
        description="Reference Identification",
        min_length=1,
        max_length=80,
    )


class TDS(Segment):
    _id: Literal["TDS"] = id_element(name="TDS")

    TotalAmount: Optional[str] = element(
        name="TDS01",
        description="Total Invoice Amount",
        min_length=1,
        max_length=15,
    )


class MTX(Segment):
    _id: Literal["MTX"] = id_element(name="MTX")

    NoteReferenceCode: Optional[str] = element(
        name="MTX01",
        description="Code identifying the functional area or purpose for which the note applies",
        min_length=1,
        max_length=3,
    )

    Text: Optional[str] = element(
        name="MTX02",
        description="To transmit large volumes of message text",
        min_length=1,
        max_length=4096,
    )

    Text2: Optional[str] = element(
        name="MTX03",
        description="To transmit large volumes of message text",
        min_length=1,
        max_length=4096,
    )

    PrinterControlCode: Optional[str] = element(
        name="MTX04",
        description="A field to be used for the control of the line feed of the receiving printer",
        min_length=2,
        max_length=2,
    )

    Number: Optional[str] = element(
        name="MTX05",
        description="A generic number",
        min_length=1,
        max_length=9,
    )

    LanguageCode: Optional[str] = element(
        name="MTX06",
        description="Code designating the language used in text (ISO 639)",
        min_length=2,
        max_length=3,
    )


class BSR(Segment):
    _id: Literal["BSR"] = id_element(name="BSR")

    StatusReportCode: Optional[str] = element(
        name="BSR01",
        description="Code indicating the reason for sending the report",
        min_length=1,
        max_length=2,
    )

    ItemCode: Optional[str] = element(
        name="BSR02",
        description="Code identifying a group of orders and items",
        min_length=2,
        max_length=2,
    )

    ReferenceID: Optional[str] = element(
        name="BSR03",
        description="Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier",
        min_length=1,
        max_length=50,
    )

    Date: Optional[str] = element(
        name="BSR04",
        description="Date expressed as CCYYMMDD where CC represents the first two digits of the calendar year",
        min_length=8,
        max_length=8,
    )


class ISR(Segment):
    _id: Literal["ISR"] = id_element(name="ISR")

    OrderStatusCode: Optional[str] = element(
        name="ISR01",
        description="Code indicating the status of an order or shipment or the disposition of any difference between the quantity ordered and the quantity shipped for a line item or transaction",
        min_length=2,
        max_length=2,
    )

    Date: Optional[str] = element(
        name="ISR02",
        description="Date expressed as CCYYMMDD where CC represents the first two digits of the calendar year",
        min_length=8,
        max_length=8,
    )

    StatusReasonCode: Optional[str] = element(
        name="ISR03",
        description="Code indicating the status reason",
        min_length=3,
        max_length=3,
    )



class SAC(Segment):
    _id: Literal["SAC"] = id_element(name="SAC")

    ChargeIndicator: Optional[str] = element(
        name="SAC01",
        description="Allowance or Charge Indicator",
        min_length=1,
        max_length=1,
    )

    SpecialServiceCode: Optional[str] = element(
        name="SAC02",
        description="Service, Promotion, Allowance, or Charge Code",
        min_length=4,
        max_length=4,
    )

    AgencyQualifier: Optional[str] = element(
        name="SAC03",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    Agency: Optional[str] = element(
        name="SAC04",
        description="Agency (SCAC Code)",
        min_length=1,
        max_length=10,
    )

    Amount: Optional[str] = element(
        name="SAC05",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    SAC06: Optional[str] = null_element(name="SAC06")

    SAC07: Optional[str] = null_element(name="SAC07")

    SAC08: Optional[str] = null_element(name="SAC08")

    SAC09: Optional[str] = null_element(name="SAC09")

    SAC10: Optional[str] = null_element(name="SAC10")

    SAC11: Optional[str] = null_element(name="SAC11")

    SAC12: Optional[str] = null_element(name="SAC12")

    ReferenceID: Optional[str] = element(
        name="SAC13",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    OptionNumber: Optional[str] = element(
        name="SAC14",
        description="Option Number",
        min_length=2,
        max_length=20,
    )

    Description: Optional[str] = element(
        name="SAC15",
        description="Description",
        min_length=1,
        max_length=80,
    )


class CTT(Segment):
    _id: Literal["CTT"] = id_element(name="CTT")

    LineCount: Optional[str] = element(
        name="CTT01",
        description="Number of Line Items",
        min_length=1,
        max_length=6,
    )


class FOB(Segment):
    _id: Literal["FOB"] = id_element(name="FOB")

    ShipmentPaymentMethod: Optional[str] = element(
        name="FOB01",
        description="Shipment Method of Payment",
        min_length=2,
        max_length=2,
    )

    LocationQualifier: Optional[str] = element(
        name="FOB02",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    Description: Optional[str] = element(
        name="FOB03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    TransportationQualifier: Optional[str] = element(
        name="FOB04",
        description="Transportation Method/Type Qualifier Code",
        min_length=2,
        max_length=2,
    )

    TransportationCode: Optional[str] = element(
        name="FOB05",
        description="Transportation Method/Type Code",
        min_length=3,
        max_length=3,
    )

    LocationQualifier2: Optional[str] = element(
        name="FOB06",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    Description2: Optional[str] = element(
        name="FOB07",
        description="Description",
        min_length=1,
        max_length=80,
    )


class PER(Segment):
    _id: Literal["PER"] = id_element(name="PER")

    ContactTypeCode: Optional[str] = element(
        name="PER01",
        description="Code identifying the major duty or responsibility of the person or group named",
        min_length=2,
        max_length=2,
    )

    Name: Optional[str] = element(
        name="PER02",
        description="Name",
        min_length=1,
        max_length=60,
    )

    CommunicationTypeCode: Optional[str] = element(
        name="PER03",
        description="Code identifying the type of communication number. TE = Telephone",
        min_length=2,
        max_length=2,
    )

    CommunicationNumber: Optional[str] = element(
        name="PER04",
        description="Communication Number",
        min_length=1,
        max_length=256,
    )

    CommunicationTypeCode2: Optional[str] = element(
        name="PER05",
        description="Code identifying the type of communication number. TE = Telephone",
        min_length=2,
        max_length=2,
    )

    CommunicationNumber2: Optional[str] = element(
        name="PER06",
        description="Name",
        min_length=1,
        max_length=80,
    )

    CommunicationTypeCode3: Optional[str] = element(
        name="PER07",
        description="Code identifying the type of communication number. TE = Telephone",
        min_length=2,
        max_length=2,
    )

    CommunicationNumber3: Optional[str] = element(
        name="PER08",
        description="Communication Number",
        min_length=1,
        max_length=80,
    )


class NTE(Segment):
    _id: Literal["NTE"] = id_element(name="NTE")

    ReferenceCode: Optional[str] = element(
        name="NTE01",
        description="Note Reference Code",
        min_length=3,
        max_length=3,
    )

    Description: Optional[str] = element(
        name="NTE02",
        description="A free-form description to clarify the related data elements and their content",
        min_length=1,
        max_length=80,
    )


class RED(Segment):
    _id: Literal["RED"] = id_element(name="RED")

    Description: Optional[str] = element(
        name="RED01",
        description="A free-form description to clarify the related data elements and their content",
        min_length=1,
        max_length=80,
    )

    RelatedID: Optional[str] = element(
        name="RED02",
        description="Related Data Identification Code",
        min_length=2,
        max_length=3,
    )


class CSH(Segment):
    _id: Literal["CSH"] = id_element(name="CSH")

    RequirementCode: str = element(
        name="CSH01",
        description="Sales Requirement Code",
        min_length=1,
        max_length=2,
    )


class ITD(Segment):
    _id: Literal["ITD"] = id_element(name="ITD")

    TypeCode: Optional[str] = element(
        name="ITD01",
        description="Terms Type Code",
        min_length=2,
        max_length=2,
    )

    BasisDateCode: Optional[str] = element(
        name="ITD02",
        description="Term basis date code",
        min_length=1,
        max_length=2,
    )

    DiscountCode: Optional[str] = element(
        name="ITD03",
        description="Terms Discount Percent",
        min_length=1,
        max_length=6,
    )

    DiscountDueDate: Optional[str] = element(
        name="ITD04",
        description="Terms Discount Due Date",
        min_length=8,
        max_length=8,
    )

    DiscountDaysDue: Optional[str] = element(
        name="ITD05",
        description="Terms Discount Days Due",
        min_length=1,
        max_length=3,
    )

    NetDueDate: Optional[str] = element(
        name="ITD06",
        description="Terms Net Due Date",
        min_length=8,
        max_length=8,
    )

    NetDays: Optional[str] = element(
        name="ITD07",
        description="Terms Net Days",
        min_length=1,
        max_length=3,
    )

    ITD08: Optional[str] = null_element(name="ITD08")

    ITD09: Optional[str] = null_element(name="ITD09")

    ITD10: Optional[str] = null_element(name="ITD10")

    ITD11: Optional[str] = null_element(name="ITD11")

    Description: Optional[str] = element(
        name="ITD12",
        description="Description",
        min_length=1,
        max_length=80,
    )


class PKG(Segment):
    _id: Literal["PKG"] = id_element(name="PKG")

    PKG01: str = element(
        name="PKG01",
        description="Item Description Type",
        min_length=1,
        max_length=1,
    )

    PKG02: Optional[str] = element(
        name="PKG02",
        description="Packaging Characteristic Code",
        min_length=1,
        max_length=5,
    )

    PKG03: Optional[str] = null_element(name="PKG03")

    PKG04: Optional[str] = null_element(name="PKG04")

    Description: str = element(
        name="PKG05",
        description="Description",
        min_length=1,
        max_length=80,
    )


class TD1(Segment):
    _id: Literal["TD1"] = id_element(name="TD1")

    PackagingCode: Optional[str] = element(
        name="TD101",
        description="Packaging Code",
        min_length=3,
        max_length=5,
    )

    LadingQuantity: Optional[str] = element(
        name="TD102",
        description="Lading Quantity",
        min_length=1,
        max_length=7
    )

    CommodityCodeQualifier: Optional[str] = element(
        name="TD103",
        description="Commodity Code Qualifier",
        min_length=1,
        max_length=1,
    )

    CommodityCode: Optional[str] = element(
        name="TD104",
        description="Commodity Code",
        min_length=1,
        max_length=1,
    )

    LadingDescription: Optional[str] = element(
        name="TD105",
        description="Lading Description",
        min_length=1,
        max_length=50,
    )

    WeightQualifier: Optional[str] = element(
        name="TD106",
        description="Weight Qualifier",
        min_length=1,
        max_length=2
    )

    Weight: Optional[str] = element(
        name="TD107",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UomCode: Optional[str] = element(
        name="TD108",
        description="Unit of Measurement Code",
        min_length=2,
        max_length=2,
    )


class TD5(Segment):
    _id: Literal["TD5"] = id_element(name="TD5")

    RelationshipQualifier: Optional[str] = element(
        name="TD501",
        description="Relationship Qualifier. 'Z' = mutually defined",
        min_length=1,
        max_length=2,
    )

    IdQualifier: Optional[str] = element(
        name="TD502",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdCode: Optional[str] = element(
        name="TD503",
        description="Identification Code - Standard Carrier Alpha Code for the carrier",
        min_length=2,
        max_length=80,
    )

    TransportationCode: Optional[str] = element(
        name="TD504",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    Routing: Optional[str] = element(
        name="TD505",
        description="Routing",
        min_length=1,
        max_length=35,
    )

    TD506: Optional[str] = null_element(name="TD506")

    LocationQualifier: Optional[str] = element(
        name="TD507",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationID: Optional[str] = element(
        name="TD508",
        description="Location Code",
        min_length=1,
        max_length=30,
    )


class N9(Segment):
    _id: Literal["N9"] = id_element(name="N9")

    IdQualifier: str = element(
        name="N901",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceID: str = element(
        name="N902",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Description: Optional[str] = element(
        name="N903",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )


class MSG(Segment):
    _id: Literal["MSG"] = id_element(name="MSG")

    Message: Optional[str] = element(
        name="MSG01",
        description="Free-Form Message Text",
        min_length=1,
        max_length=1,
    )


class N1(Segment):
    _id: Literal["N1"] = id_element(name="N1")

    TypeCode: str = element(
        name="N101",
        description="Entity Identifier Code: BY=Buying Party, SF=Ship From, ST=Ship To",
        min_length=2,
        max_length=3,
    )

    Name: Optional[str] = element(
        name="N102",
        description="name",
        min_length=1,
        max_length=60,
    )

    IdCodeQualifier: Optional[str] = element(
        name="N103",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=35,
    )

    IdCode: Optional[str] = element(
        name="N104",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )


class N2(Segment):
    _id: Literal["N2"] = id_element(name="N2")

    Name2: Optional[str] = element(
        name="N201",
        description="extra name",
        min_length=1,
        max_length=60,
    )

    Name3: Optional[str] = element(
        name="N202",
        description="extra name",
        min_length=1,
        max_length=60,
    )


class N3(Segment):
    _id: Literal["N3"] = id_element(name="N3")

    AddressLine1: str = element(
        name="N301",
        description="Address Information",
        min_length=1,
        max_length=55,
    )

    AddressLine2: Optional[str] = element(
        name="N302",
        description="Address Information",
        min_length=1,
        max_length=55,
    )


class N4(Segment):
    _id: Literal["N4"] = id_element(name="N4")

    City: str = element(
        name="N401",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    State: str = element(
        name="N402",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    PostalCode: str = element(
        name="N403",
        description="Postal Code - Code defining international postal zone code excluding punctuation and blanks",
        min_length=3,
        max_length=15,
    )

    Country: Optional[str] = element(
        name="N404",
        description="Country Code",
        min_length=2,
        max_length=3,
    )


class PO1(Segment):
    _id: Literal["PO1"] = id_element(name="PO1")

    LineID: Optional[str] = element(
        name="PO101",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    Quantity: Optional[str] = element(
        name="PO102",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UOM: Optional[str] = element(
        name="PO103",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    UnitPrice: Optional[str] = element(
        name="PO104",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    UnitPriceCode: Optional[str] = element(
        name="PO105",
        description="Basis of Unit Price Code",
        min_length=2,
        max_length=2,
    )

    ItemIdQualifier: Optional[str] = element(
        name="PO106",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID: Optional[str] = element(
        name="PO107",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier2: Optional[str] = element(
        name="PO108",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID2: Optional[str] = element(
        name="PO109",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier3: Optional[str] = element(
        name="PO110",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID3: Optional[str] = element(
        name="PO111",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier4: Optional[str] = element(
        name="PO112",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID4: Optional[str] = element(
        name="PO113",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier5: Optional[str] = element(
        name="PO114",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID5: Optional[str] = element(
        name="PO115",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )


class BSN(Segment):
    _id: Literal["BSN"] = id_element(name="BSN")

    PurposeCode: str = element(
        name="BSN01",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    ShipmentID: str = element(
        name="BSN02",
        description="Shipment Identification",
        min_length=2,
        max_length=30,
    )

    ShipDate: str = element(
        name="BSN03",
        description="Date Shipped",
        min_length=8,
        max_length=8,
    )

    ShipTime: str = element(
        name="BSN04",
        description="Time Shipped",
        min_length=6,
        max_length=8,
    )

    HierarchicalStructureCode: str = element(
        name="BSN05",
        description="Hierarchical Structure Code",
        min_length=4,
        max_length=4,
    )


class HL(Segment):
    _id: Literal["HL"] = id_element(name="HL")

    HierarchicalID: str = element(
        name="HL01",
        description="Hierarchical ID Number",
        min_length=1,
        max_length=12,
    )

    ParentID: Optional[str] = element(
        name="HL02",
        description="Hierarchical Parent ID Number",
        min_length=1,
        max_length=12,
    )

    HierarchicalLevel: str = element(
        name="HL03",
        description="Hierarchical Level Code: S=shipment, O=order, I=item, P=package",
        min_length=1,
        max_length=2,
    )


class PRF(Segment):
    _id: Literal["PRF"] = id_element(name="PRF")

    OrderID: str = element(
        name="PRF01",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )


from typing import Optional, Literal

class LIN(Segment):
    _id: Literal["LIN"] = id_element(name="LIN")

    LineID: str = element(
        name="LIN01",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    ItemIdQualifier: str = element(
        name="LIN02",
        description="Product/Service ID Qualifier. VN=Supplier Product Number",
        min_length=2,
        max_length=2,
    )

    ItemID: str = element(
        name="LIN03",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier2: Optional[str] = element(
        name="LIN04",
        description="Product/Service ID Qualifier. IM=Imprint Number, UP=Consumer Package code",
        min_length=2,
        max_length=2,
    )

    ItemID2: Optional[str] = element(
        name="LIN05",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier3: Optional[str] = element(name="LIN06", description="Product/Service ID Qualifier", min_length=2, max_length=2)
    ItemID3: Optional[str] = element(name="LIN07", description="Product/Service ID", min_length=1, max_length=48)

    ItemIdQualifier4: Optional[str] = element(name="LIN08", description="Product/Service ID Qualifier", min_length=2, max_length=2)
    ItemID4: Optional[str] = element(name="LIN09", description="Product/Service ID", min_length=1, max_length=48)

    ItemIdQualifier5: Optional[str] = element(name="LIN10", description="Product/Service ID Qualifier", min_length=2, max_length=2)
    ItemID5: Optional[str] = element(name="LIN11", description="Product/Service ID", min_length=1, max_length=48)

    ItemIdQualifier6: Optional[str] = element(name="LIN12", description="Product/Service ID Qualifier", min_length=2, max_length=2)
    ItemID6: Optional[str] = element(name="LIN13", description="Product/Service ID", min_length=1, max_length=48)

    ItemIdQualifier7: Optional[str] = element(name="LIN14", description="Product/Service ID Qualifier", min_length=2, max_length=2)
    ItemID7: Optional[str] = element(name="LIN15", description="Product/Service ID", min_length=1, max_length=48)

    ItemIdQualifier8: Optional[str] = element(name="LIN16", description="Product/Service ID Qualifier", min_length=2, max_length=2)
    ItemID8: Optional[str] = element(name="LIN17", description="Product/Service ID", min_length=1, max_length=48)

    ItemIdQualifier9: Optional[str] = element(name="LIN18", description="Product/Service ID Qualifier", min_length=2, max_length=2)
    ItemID9: Optional[str] = element(name="LIN19", description="Product/Service ID", min_length=1, max_length=48)

    ItemIdQualifier10: Optional[str] = element(name="LIN20", description="Product/Service ID Qualifier", min_length=2, max_length=2)
    ItemID10: Optional[str] = element(name="LIN21", description="Product/Service ID", min_length=1, max_length=48)

    ItemIdQualifier11: Optional[str] = element(name="LIN22", description="Product/Service ID Qualifier", min_length=2, max_length=2)
    ItemID11: Optional[str] = element(name="LIN23", description="Product/Service ID", min_length=1, max_length=48)

    ItemIdQualifier12: Optional[str] = element(name="LIN24", description="Product/Service ID Qualifier", min_length=2, max_length=2)
    ItemID12: Optional[str] = element(name="LIN25", description="Product/Service ID", min_length=1, max_length=48)

    ItemIdQualifier13: Optional[str] = element(name="LIN26", description="Product/Service ID Qualifier", min_length=2, max_length=2)
    ItemID13: Optional[str] = element(name="LIN27", description="Product/Service ID", min_length=1, max_length=48)

    ItemIdQualifier14: Optional[str] = element(name="LIN28", description="Product/Service ID Qualifier", min_length=2, max_length=2)
    ItemID14: Optional[str] = element(name="LIN29", description="Product/Service ID", min_length=1, max_length=48)

    ItemIdQualifier15: Optional[str] = element(name="LIN30", description="Product/Service ID Qualifier", min_length=2, max_length=2)
    ItemID15: Optional[str] = element(name="LIN31", description="Product/Service ID", min_length=1, max_length=48)



class SN1(Segment):
    _id: Literal["SN1"] = id_element(name="SN1")

    LineID: str = element(
        name="SN101",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    UnitsShippedCount: Optional[str] = element(
        default="0",
        name="SN102",
        description="Number of Units Shipped",
        min_length=1,
        max_length=10,
    )

    UOM: str = element(
        name="SN103",
        description="Unit or Basis for Measurement Code. EA=Each",
        min_length=2,
        max_length=2,
    )


class MAN(Segment):
    _id: Literal["MAN"] = id_element(name="MAN")

    Qualifier: Optional[str] = element(
        name="MAN01",
        description="Marks and Numbers Qualifier",
        min_length=1,
        max_length=2,
    )

    Number: Optional[str] = element(
        name="MAN02",
        description="Marks and numbers",
        min_length=1,
        max_length=48,
    )

    MAN03: Optional[str] = null_element(name="MAN03")

    Qualifier2: Optional[str] = element(
        name="MAN04",
        description="marks and numbers qualifier",
        min_length=1,
        max_length=2,
    )

    Number2: Optional[str] = element(
        name="MAN05",
        description="marks and numbers",
        min_length=1,
        max_length=48,
    )


class CTB(Segment):
    _id: Literal["CTB"] = id_element(name="CTB")

    RestrictionsQualifier: str = element(
        name="CTB01",
        description="Restrictions Qualifier",
        min_length=2,
        max_length=2,
    )

    Description: Optional[str] = element(
        name="CTB02",
        description="Description",
        min_length=1,
        max_length=80,
    )


class AMT(Segment):
    _id: Literal["AMT"] = id_element(name="AMT")

    AmountQualifier: str = element(
        name="AMT01",
        description="Monetary Amount Qualifier",
        min_length=1,
        max_length=6,
    )

    TotalAmount: str = element(
        name="AMT02",
        description="Monetary Amount summary",
        min_length=1,
        max_length=18,
    )


class BGN(Segment):
    _id: Literal["BGN"] = id_element(name="BGN")

    PurposeCode: str = element(
        name="BGN01",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    ReferenceID: str = element(
        name="BGN02",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Date: str = element(
        name="BGN03",
        description="Date",
        min_length=8,
        max_length=8,
    )


class OTI(Segment):
    _id: Literal["OTI"] = id_element(name="OTI")

    AcknowledgmentCode: str = element(
        name="OTI01",
        description="Application Acknowledgment Code",
        min_length=1,
        max_length=2,
    )

    ReferenceIdQualifier: str = element(
        name="OTI02",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceID: str = element(
        name="OTI03",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    OTI04: Optional[str] = null_element(name="OTI04")

    OTI05: Optional[str] = null_element(name="OTI05")

    OTI06: Optional[str] = null_element(name="OTI06")

    OTI07: Optional[str] = null_element(name="OTI07")

    GroupControlNumber: Optional[str] = element(
        name="OTI08",
        description="Group Control Number",
        min_length=1,
        max_length=9,
    )

    TransactionSetControlNumber: Optional[str] = element(
        name="OTI09",
        description="Transaction Set Control Number",
        min_length=4,
        max_length=9,
    )

    TransactionSetID: Optional[str] = element(
        name="OTI10",
        description="Transaction Set Identifier Code",
        min_length=3,
        max_length=3,
    )


class TED(Segment):
    _id: Literal["TED"] = id_element(name="TED")

    TED01: str = element(
        name="TED01",
        description="Application Error Condition Code",
        min_length=1,
        max_length=3,
    )

    TED02: Optional[str] = element(
        name="TED02",
        description="Free-form Message",
        min_length=1,
        max_length=60,
    )


class AK1(Segment):
    _id: Literal["AK1"] = id_element(name="AK1")

    GroupCode: str = element(
        name="AK101",
        description="Functional ID Code",
        min_length=2,
        max_length=2,
    )

    GroupID: str = element(
        name="AK102",
        description="Data Interchange Control Number",
        min_length=1,
        max_length=9,
    )


class AK2(Segment):
    _id: Literal["AK2"] = id_element(name="AK2")

    TransactionSetCode: str = element(
        name="AK201",
        description="Transaction Set ID",
        min_length=3,
        max_length=3,
    )

    TransactionSetID: str = element(
        name="AK202",
        description="Transaction Set Control Number",
        min_length=1,
        max_length=9,
    )


class AK3(Segment):
    _id: Literal["AK3"] = id_element(name="AK3")

    SegmentID: str = element(
        name="AK301",
        description="Segment ID Code",
        min_length=2,
        max_length=3,
    )

    SegmentPosition: str = element(
        name="AK302",
        description="Segment Position in Transaction Set",
        min_length=1,
        max_length=6,
    )

    LoopID: Optional[str] = element(
        name="AK303",
        description="Loop Identifier Code",
        min_length=1,
        max_length=4,
    )

    ErrorCode: Optional[str] = element(
        name="AK304",
        description="Segment Syntax Error Code",
        min_length=1,
        max_length=3,
    )


class AK4(Segment):
    _id: Literal["AK4"] = id_element(name="AK4")

    ElementPosition: str = element(
        name="AK401",
        description="Position in Segment",
        min_length=1,
        max_length=3,
    )

    ElementReferenceID: Optional[str] = element(
        name="AK402",
        description="Data Element Reference Number",
        min_length=1,
        max_length=4,
    )

    ErrorCode: str = element(
        name="AK403",
        description="Data Element Syntax Error Codes",
        min_length=1,
        max_length=3,
    )

    ElementCopy: Optional[str] = element(
        name="AK404",
        description="Copy of Bad Data Element",
        min_length=1,
        max_length=99,
    )


class AK5(Segment):
    _id: Literal["AK5"] = id_element(name="AK5")

    AcknowledgementCode: str = element(
        name="AK501",
        description="Set Acknowledgement Code",
        min_length=1,
        max_length=1,
    )

    ErrorCode: Optional[str] = element(
        name="AK502",
        description="Transaction Set Syntax Error Code",
        min_length=1,
        max_length=3,
    )

    ErrorCode2: Optional[str] = element(
        name="AK503",
        description="Transaction Set Syntax Error Code",
        min_length=1,
        max_length=3,
    )

    ErrorCode3: Optional[str] = element(
        name="AK504",
        description="Transaction Set Syntax Error Code",
        min_length=1,
        max_length=3,
    )

    ErrorCode4: Optional[str] = element(
        name="AK505",
        description="Transaction Set Syntax Error Code",
        min_length=1,
        max_length=3,
    )

    ErrorCode5: Optional[str] = element(
        name="AK506",
        description="Transaction Set Syntax Error Code",
        min_length=1,
        max_length=3,
    )


class AK9(Segment):
    _id: Literal["AK9"] = id_element(name="AK9")

    AcknowledgementCode: str = element(
        name="AK901",
        description="Group Acknowledgement Code",
        min_length=1,
        max_length=1,
    )

    TransactionSetsCount: str = element(
        name="AK902",
        description="Number of Included Sets",
        min_length=1,
        max_length=6,
    )

    ReceivedCount: str = element(
        name="AK903",
        description="Number of Received Sets",
        min_length=1,
        max_length=6,
    )

    AcceptedCount: str = element(
        name="AK904",
        description="Number of Accepted Sets",
        min_length=1,
        max_length=6,
    )

    ErrorCode: Optional[str] = element(
        name="AK905",
        description="Functional Group Syntax Error Code",
        min_length=1,
        max_length=3,
    )

    ErrorCode2: Optional[str] = element(
        name="AK906",
        description="Functional Group Syntax Error Code",
        min_length=1,
        max_length=3,
    )

    ErrorCode3: Optional[str] = element(
        name="AK907",
        description="Functional Group Syntax Error Code",
        min_length=1,
        max_length=3,
    )

    ErrorCode4: Optional[str] = element(
        name="AK908",
        description="Functional Group Syntax Error Code",
        min_length=1,
        max_length=3,
    )

    ErrorCode5: Optional[str] = element(
        name="AK909",
        description="Functional Group Syntax Error Code",
        min_length=1,
        max_length=3,
    )


class BAK(Segment):
    _id: Literal["BAK"] = id_element(name="BAK")

    TransactionSetPurpose: str = element(
        name="BAK01",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    Acknowledgment: str = element(
        name="BAK02",
        description="Acknowledgment Type",
        min_length=2,
        max_length=2,
    )

    PurchaseOrderID: str = element(
        name="BAK03",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    PurchaseOrderDate: str = element(
        name="BAK04",
        description="Purchase Order Date",
        min_length=8,
        max_length=8,
    )

    BAK05: Optional[str] = null_element(name="BAK05")

    BAK06: Optional[str] = null_element(name="BAK06")

    BAK07: Optional[str] = null_element(name="BAK07")

    ReferenceID: Optional[str] = element(
        name="BAK08",
        description="Reference",
        min_length=1,
        max_length=30,
    )

    AcknowledgmentDate: Optional[str] = element(
        name="BAK09",
        description="Acknowledgment Date",
        min_length=8,
        max_length=8,
    )


class CTP(Segment):
    _id: Literal["CTP"] = id_element(name="CTP")

    CTP01: Optional[str] = null_element(name="CTP01")

    PriceCode: Optional[str] = element(
        name="CTP02",
        description="Code identifying pricing specification",
        min_length=3,
        max_length=3,
    )

    Price: Optional[str] = element(
        name="CTP03",
        description="Price per unit of product, service, commodity, etc.",
        min_length=1,
        max_length=17,
    )

    CTP04: Optional[str] = null_element(name="CTP04")

    CTP05: Optional[str] = null_element(name="CTP05")

    CTP06: Optional[str] = null_element(name="CTP06")

    CTP07: Optional[str] = null_element(name="CTP07")

    MonetaryAmount: Optional[str] = element(
        name="CTP08",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    CTP09: Optional[str] = null_element(name="CTP09")




class CAD(Segment):
    _id: Literal["CAD"] = id_element(name="CAD")

    TransportationMethod: str = element(
        name="CAD01",
        description="Code specifying the method or type of transportation for the shipment",
        min_length=1,
        max_length=2,
    )

    CAD02: Optional[str] = null_element(name="CAD02")

    CAD03: Optional[str] = null_element(name="CAD03")

    AlphaCode: str = element(
        name="CAD04",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    Routing: str = element(
        name="CAD05",
        description="Free-form description of the routing or requested routing for shipment, or the originating carrier's identity",
        min_length=1,
        max_length=35,
    )

    CAD06: Optional[str] = null_element(name="CAD06")

    ReferenceIdQualifier: str = element(
        name="CAD07",
        description="Code qualifying the Reference Identification",
        min_length=2,
        max_length=3,
    )

    ReferenceID: Optional[str] = element(
        name="CAD08",
        description="Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier",
        min_length=1,
        max_length=30,
    )

    ServiceLevelCode: Optional[str] = element(
        name="CAD09",
        description="Code indicating the level of transportation service or the billing service offered by the transportation carrier",
        min_length=2,
        max_length=2,
    )


class PO4(Segment):
    _id: Literal["PO4"] = id_element(name="PO4")

    ContainerCount: Optional[str] = element(
        name="PO401",
        description="The number of inner containers, or number of eaches if there are no inner containers, per outer container",
        min_length=1,
        max_length=6,
    )

    PO402: Optional[str] = null_element(name="PO402")

    PO403: Optional[str] = null_element(name="PO403")

    PO404: Optional[str] = null_element(name="PO404")

    PO405: Optional[str] = null_element(name="PO405")

    PO406: Optional[str] = null_element(name="PO406")

    PO407: Optional[str] = null_element(name="PO407")

    PO408: Optional[str] = null_element(name="PO408")

    PO409: Optional[str] = null_element(name="PO409")

    PO410: Optional[str] = null_element(name="PO410")

    PO411: Optional[str] = null_element(name="PO411")

    PO412: Optional[str] = null_element(name="PO412")

    PO413: Optional[str] = null_element(name="PO413")

    UnitsPerContainer: Optional[str] = element(
        name="PO414",
        description="The number of eaches per inner container",
        min_length=1,
        max_length=6,
    )


class SDQ(Segment):
    _id: Literal["SDQ"] = id_element(name="SDQ")

    UOM: str = element(
        name="SDQ01",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    IdCodeQualifier: Optional[str] = element(
        name="SDQ02",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdCode: str = element(
        name="SDQ03",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity: str = element(
        name="SDQ04",
        description="Numeric value of quantity",
        min_length=1,
        max_length=15,
    )

    IdCode2: Optional[str] = element(
        name="SDQ05",
        description="Code identifying a party or other code",
        min_length=2,
        max_length=80,
    )

    Quantity2: Optional[str] = element(
        name="SDQ06",
        description="Numeric value of quantity",
        min_length=1,
        max_length=15,
    )

    IdCode3: Optional[str] = element(
        name="SDQ07",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity3: Optional[str] = element(
        name="SDQ08",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IdCode4: Optional[str] = element(
        name="SDQ09",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity4: Optional[str] = element(
        name="SDQ10",
        description="Numeric value of quantity",
        min_length=1,
        max_length=15,
    )

    IdCode5: Optional[str] = element(
        name="SDQ11",
        description="Code identifying a party or other code",
        min_length=2,
        max_length=80,
    )

    Quantity5: Optional[str] = element(
        name="SDQ12",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IdCode6: Optional[str] = element(
        name="SDQ13",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity6: Optional[str] = element(
        name="SDQ14",
        description="Numeric value of quantity",
        min_length=1,
        max_length=15,
    )

    IdCode7: Optional[str] = element(
        name="SDQ15",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity7: Optional[str] = element(
        name="SDQ16",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IdCode8: Optional[str] = element(
        name="SDQ17",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity8: Optional[str] = element(
        name="SDQ18",
        description="Numeric value of quantity",
        min_length=1,
        max_length=15,
    )

    IdCode9: Optional[str] = element(
        name="SDQ19",
        description="Code identifying a party or other code",
        min_length=2,
        max_length=80,
    )

    Quantity9: Optional[str] = element(
        name="SDQ20",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IdCode10: Optional[str] = element(
        name="SDQ21",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity10: Optional[str] = element(
        name="SDQ22",
        description="Numeric value of quantity",
        min_length=1,
        max_length=15,
    )


class ACK(Segment):
    _id: Literal["ACK"] = id_element(name="ACK")

    ItemStatus: str = element(
        name="ACK01",
        description="Line Item Status Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[str] = element(
        name="ACK02",
        description="Numeric value of quantity",
        min_length=1,
        max_length=15,
    )

    UOM: Optional[str] = element(
        name="ACK03",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    DateTimeQualifier: str = element(
        name="ACK04",
        description="Code specifying type of date or time, or both date and time",
        min_length=3,
        max_length=3,
    )

    Date: Optional[str] = element(
        name="ACK05",
        description="Date expressed as CCYYMMDD where CC represents the first two digits of the calendar year",
        min_length=8,
        max_length=8,
    )
