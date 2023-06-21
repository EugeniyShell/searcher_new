from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Substantion(db.Model):
    __tablename__ = 'grls'
    id = db.Column(db.Integer, primary_key=True)
    commonname_normalized = db.Column(db.String(255))
    commonname = db.Column(db.String(255))
    drugname_normalized = db.Column(db.String(255))
    drugname = db.Column(db.String(255))


def base_search(src):
    help_mnn = Substantion.query.filter(
        Substantion.drugname_normalized.contains(src.lower())
    ).all()
    mnn_list = [item.commonname for item in help_mnn] + [src]
    res_list = []
    for mnn in mnn_list:
        temp = Substantion.query.filter(
            Substantion.commonname_normalized.contains(mnn.lower())
        ).all()
        res_list += [item.drugname for item in temp]
    res_list += mnn_list
    return list(set(res_list))
