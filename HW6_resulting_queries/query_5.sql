SELECT sbj.subj_name FROM teachers t INNER JOIN subjects sbj on t.id =sbj.teacher_id WHERE t.teacher_name  = :teacher_name GROUP BY sbj.subj_name