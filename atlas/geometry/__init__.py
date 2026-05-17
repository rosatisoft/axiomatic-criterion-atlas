from atlas.geometry.svd_basis import (
    SVDBasis,
    build_svd_basis,
    estimate_rank_from_energy,
    validate_orthonormal_basis,
)

from atlas.geometry.projection import (
    project_onto_basis,
    residual_from_basis,
    projection_norm,
    residual_norm,
    projection_ratio,
)

from atlas.geometry.origin_cost import (
    OriginCostResult,
    compute_origin_cost,
    origin_cost_value,
    normalized_origin_cost,
)

from atlas.geometry.field_selection import (
    FieldScore,
    FieldSelectionResult,
    evaluate_fields,
    select_field,
    dominant_field,
    field_margin,
)