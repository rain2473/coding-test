SELECT A.CAR_ID
     , A.CAR_TYPE
     , TRUNC(A.DAILY_FEE * 30 * (100 - DISCOUNT_RATE) / 100) AS FEE
  FROM (
        SELECT *
          FROM CAR_RENTAL_COMPANY_CAR A
         WHERE 1 = 1
           AND NOT EXISTS (
                          SELECT *
                            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY B
                           WHERE A.CAR_ID = B.CAR_ID
                             AND ( 
                                  TO_DATE('20221101', 'YYYYMMDD') BETWEEN START_DATE AND END_DATE - 1
                              OR  TO_DATE('20221130', 'YYYYMMDD') BETWEEN START_DATE + 1 AND END_DATE
                                 )
                          ) 
       ) A,
       (
        SELECT 
               PLAN_ID
             , CAR_TYPE
             , DISCOUNT_RATE
          FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
         WHERE DURATION_TYPE = '30일 이상'
       ) C
 WHERE A.CAR_TYPE = C.CAR_TYPE
   AND TRUNC(A.DAILY_FEE * 30 * (100 - DISCOUNT_RATE) / 100) BETWEEN 500000 AND 2000000
 ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC
;