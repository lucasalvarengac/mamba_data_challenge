SELECT
    SPLIT(utm, '-')[safe_ordinal(2)] as source, count(cpf) as users
FROM
    `begrowth-user-api-demo.bg_users.bg_data_enginner_test_lucasAlvarenga`
GROUP BY
    1
ORDER BY
    1 ASC
