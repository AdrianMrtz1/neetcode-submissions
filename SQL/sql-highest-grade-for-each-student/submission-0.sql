SELECT student_id, exam_id, score
FROM (
    SELECT student_id, exam_id, score, ROW_NUMBER() OVER (
        PARTITION BY student_id ORDER BY score DESC, exam_id ASC) as exam_rank
        FROM exam_results) as student_ranks
WHERE exam_rank = 1
ORDER BY student_id ASC