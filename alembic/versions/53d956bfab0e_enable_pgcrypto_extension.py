"""Enable pgcrypto extension

Revision ID: 53d956bfab0e
Revises: 1c4d33b3e6c0
Create Date: 2023-06-11 09:17:06.530581

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = '53d956bfab0e'
down_revision = '1c4d33b3e6c0'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(text("CREATE EXTENSION IF NOT EXISTS pgcrypto;"))


def downgrade():
    op.execute(text("DROP EXTENSION IF EXISTS pgcrypto;"))
