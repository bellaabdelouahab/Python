select constraint_name,constraint_type,search_condition
from user_constraints 
where table_name='COUNTRIES';



ALTER TABLE departments    ENABLE CONSTRAINT depa2_ref;