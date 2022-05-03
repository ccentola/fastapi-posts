"""add relationsip between posts and users

Revision ID: 28476f19199f
Revises: 3f83789fc9db
Create Date: 2022-05-01 15:20:16.170349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "28476f19199f"
down_revision = "3f83789fc9db"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
