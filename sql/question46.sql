WITH bg_data AS (
    SELECT
        id,
        first_name,
        last_name,
        email,
        gender,
        address_geo_latitude,
        address_geo_longitude,
        address_country,
        NORMALIZE(address_state) as address_state, # convertendo para ascii
        utm,
        cpf,
        CAST(right(concat(cpf),1) AS INT64) as cpf_last_digit,
        dt_insert,
        candidate_name
    FROM
        `begrowth-user-api-demo.bg_users.bg_data_enginner_test_lucasAlvarenga`
)

SELECT
    bg_data.*,
    cpf_state.uf as state,
    brazilian_state.initials as initials,
    REGEXP_CONTAINS(cpf_state.uf, brazilian_state.initials) as same_state
FROM
    bg_data
LEFT JOIN
    `begrowth-user-api-demo.bg_users.cpf_state` as cpf_state
ON  
    bg_data.cpf_last_digit = cpf_state.id
LEFT JOIN
    begrowth-user-api-demo.bg_users.brazilian_state as brazilian_state
ON
    bg_data.address_state = brazilian_state.uf
