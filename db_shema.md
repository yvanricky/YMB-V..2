```markdown
# db_schema.md

## Table: users

| Colonne        | Type        |
|----------------|-------------|
| id             | UUID        |
| telegram_id    | TEXT        |
| username       | TEXT        |
| is_subscribed  | BOOLEAN     |
| plan           | TEXT        |
| created_at     | TIMESTAMP   |

## Table: transactions

| Colonne        | Type        |
|----------------|-------------|
| id             | UUID        |
| user_id        | UUID        |
| method         | TEXT        |
| status         | TEXT        |
| amount         | NUMERIC     |
| created_at     | TIMESTAMP   |

## Table: pronostics

| Colonne        | Type        |
|----------------|-------------|
| id             | UUID        |
| match          | TEXT        |
| prediction     | TEXT        |
| confidence     | INTEGER     |
| published_at   | TIMESTAMP   |

## Table: messages_log

| Colonne        | Type        |
|----------------|-------------|
| id             | UUID        |
| user_id        | UUID        |
| content        | TEXT        |
| response       | TEXT        |
| sent_at        | TIMESTAMP   |
```
