from enum import Enum


class TaxModesEnum(int, Enum):
    tax_farm_mode = 1  # 'Налоговый режим для крестьянских и фермерских хозяйств'
    tax_low_too_mode = 2  # 'Налоговый режим для малых предприятий на основе патента'
    tax_general_mode = 3  # 'Общеустановленная система налогообложения'
    tax_simplified_mode = 4  # 'Упрощенная система налогообложения'


class MemberTypesEnum(str, Enum):
    owner = 'владелец'
    analytic = 'аналитик'


class NDSTypesEnum(int, Enum):
    nds_inside = 0  # 'В том числе'
    nds_outside = 1  # 'Сверху'
