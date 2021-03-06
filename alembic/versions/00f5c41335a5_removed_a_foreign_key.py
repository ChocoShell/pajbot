"""removed a foreign key

Revision ID: 00f5c41335a5
Revises: c1c83c09da93
Create Date: 2016-03-03 14:40:56.689710

"""

# revision identifiers, used by Alembic.
revision = '00f5c41335a5'
down_revision = 'c1c83c09da93'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tb_stream_chunk_highlight_ibfk_2', 'tb_stream_chunk_highlight', type_='foreignkey')
    op.drop_constraint('tb_stream_chunk_highlight_ibfk_3', 'tb_stream_chunk_highlight', type_='foreignkey')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('tb_stream_chunk_highlight_ibfk_3', 'tb_stream_chunk_highlight', 'tb_user', ['last_edited_by'], ['id'])
    op.create_foreign_key('tb_stream_chunk_highlight_ibfk_2', 'tb_stream_chunk_highlight', 'tb_user', ['created_by'], ['id'])
    ### end Alembic commands ###
