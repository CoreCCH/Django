USE `test1`;
CREATE VIEW `question_choice_view` AS 
SELECT q.question_text, q.pub_date, c.choice_text, c.votes
FROM polls_question as q INNER JOIN polls_choice AS c ON q.id = c.question.id;