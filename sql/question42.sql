SELECT
    address_state, count(distinct cpf) as unique_users
FROM
    `begrowth-user-api-demo.bg_users.bg_data_enginner_test_lucasAlvarenga`
GROUP BY
    1
ORDER BY
    2 DESC
