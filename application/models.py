import datetime

from sqlalchemy import desc
from sqlalchemy import or_

from application import db


class SampleTable(db.Model):
    __tablename__ = "SampleTasksTable"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text())
    added_time = db.Column(db.DateTime, default=datetime.datetime.now)

    def get_id(self, some_id):
        record = SampleTable.query.filter(SampleTable.id == some_id).first_or_404()
        aux = dict()
        aux['id'] = record.id
        aux['title'] = record.title
        aux['description'] = record.description
        aux['added_time'] = record.added_time
        return aux


    def add_data(self, title, description):
        new_record = SampleTable(title=title, description=description)
        db.session.add(new_record)
        db.session.commit()


    def list_all(self, page, LISTINGS_PER_PAGE):
        return SampleTable.query.order_by(desc(SampleTable.added_time)).paginate(page, LISTINGS_PER_PAGE, False)


    # ------ Delete them if you don't plan to use them ----------

    def benchmark_searchspeed(self):
        # my very stupid benchmark
        records = SampleTable.query.filter(
                or_(SampleTable.description.like('%ab%'), SampleTable.description.like('%10%'))).order_by(
                desc(SampleTable.added_time)).limit(500)
        output = list()
        for record in records:
            second = SampleTable.query.filter(SampleTable.description.contains(record.title[0:1])).first()
            if second:
                aux = dict()
                aux['id'] = second.id
                aux['title'] = second.title
                aux['description'] = second.description
                aux['added_time'] = second.added_time
                output.append(aux)
        return output


    def __str__(self):
        return '<SampleTable %r, %s>' % (self.id, self.title)
