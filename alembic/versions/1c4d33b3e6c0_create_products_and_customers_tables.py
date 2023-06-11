"""Create products and customers tables

Revision ID: 1c4d33b3e6c0
Revises: 
Create Date: 2023-06-11 09:09:19.982243

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '1c4d33b3e6c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column("id", UUID(as_uuid=True), primary_key=True,
                  index=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("name", sa.String, index=True),
        sa.Column("description", sa.String),
        sa.Column("price", sa.Float),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, server_onupdate=sa.func.now()),
    )

    op.create_table(
        "customers",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, index=True,
                  server_default=sa.text("gen_random_uuid()")),  # Update this line
        sa.Column("name", sa.String, index=True),
        sa.Column("email", sa.String),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, server_onupdate=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table("products")
    op.drop_table("customers")
