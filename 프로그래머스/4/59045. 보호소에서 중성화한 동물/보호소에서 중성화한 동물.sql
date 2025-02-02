-- 코드를 입력하세요
SELECT A.ANIMAL_ID
     , A.ANIMAL_TYPE
     , A.NAME
  FROM ANIMAL_INS A
     , ANIMAL_OUTS B
 WHERE A.ANIMAL_ID = B.ANIMAL_ID
   AND SUBSTRB(SEX_UPON_INTAKE, 1, INSTR(SEX_UPON_INTAKE, ' ', 1, 1) - 1) IN ('Intact')
   AND SUBSTRB(SEX_UPON_OUTCOME, 1, INSTR(SEX_UPON_OUTCOME, ' ', 1, 1) - 1) NOT IN ('Intact')
 ORDER BY ANIMAL_ID