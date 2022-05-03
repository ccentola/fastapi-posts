"""add content column to post table

Revision ID: badca70d9430
Revises: 2ca35f51cf04
Create Date: 2022-05-01 15:07:07.588183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "badca70d9430"
down_revision = "2ca35f51cf04"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")
