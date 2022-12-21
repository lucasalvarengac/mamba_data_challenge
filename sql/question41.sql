SELECT
    address_state, count(id) as users
FROM
    `begrowth-user-api-demo.bg_users.bg_data_enginner_test_lucasAlvarenga`
GROUP BY
    1
ORDER BY
    2 DESC
