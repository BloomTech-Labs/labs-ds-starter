"""
Labs DS Data Engineer Role
- Database Interface
- Visualization Interface
"""
import os
import re
import string
from random import randint
from typing import Iterable, Dict, List

import pandas as pd
import psycopg2
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objs import Figure
from psycopg2 import sql
from dotenv import load_dotenv


class Data:
    load_dotenv()
    db_url = os.getenv("DB_URL")

    def _setup(self, table_name: str, columns: Iterable[str]):
        self._action(f"""CREATE TABLE IF NOT EXISTS {table_name} 
        ({', '.join(columns)});""")

    def _action(self, sql_action):
        conn = psycopg2.connect(self.db_url)
        curs = conn.cursor()
        curs.execute(sql_action)
        conn.commit()
        curs.close()
        conn.close()

    def _query(self, sql_query) -> list:
        conn = psycopg2.connect(self.db_url)
        curs = conn.cursor()
        curs.execute(sql_query)
        results = curs.fetchall()
        curs.close()
        conn.close()
        return results

    def count(self) -> int:
        return self._query("SELECT COUNT(*) FROM features")[0][0]

    def columns(self) -> List[str]:
        return [col[3] for col in self._query(
            """SELECT * FROM information_schema.columns 
            WHERE table_name = 'features';"""
        )]

    def rows(self) -> List[List]:
        return self._query("SELECT * FROM features;")

    def df(self):
        return pd.DataFrame(data=self.rows(), columns=self.columns())

    def row(self, idx: int) -> Dict:
        df = self.df()
        return df[df["idx"] == idx].to_dict(orient="records")[0]

    def format_target(self, target):
        return f"Class {str(target).rjust(2, '0')}"

    def random_row(self, n_features=3):
        features = tuple(randint(1, 6) for _ in range(n_features))
        return *features, self.format_target(sum(features))

    def joined_rows(self, n_rows):
        return ",".join(str(self.random_row()) for _ in range(n_rows))

    def seed(self, n_rows: int):
        self._action(f"""INSERT INTO
        features (feature_1, feature_2, feature_3, target)
        VALUES {self.joined_rows(n_rows)};""")

    @staticmethod
    def cleaner(text: str) -> str:
        return re.sub(r"\s+", " ", text.translate(
            str.maketrans("", "", string.punctuation)
        ).strip())

    def insert(self, feature_1, feature_2, feature_3, target):
        self._action(sql.SQL("""INSERT INTO features
        (feature_1, feature_2, feature_3, target)
        VALUES ({},{},{},{});""").format(
            sql.Literal(feature_1),
            sql.Literal(feature_2),
            sql.Literal(feature_3),
            sql.Literal(self.format_target(self.cleaner(target))),
        ))
        return int(self._query(sql.SQL("""SELECT idx FROM features 
            ORDER BY idx DESC LIMIT 1;"""))[0][0])

    def reset(self):
        self._action("TRUNCATE TABLE features RESTART IDENTITY;")

    def crosstab_vis(self, feature_id) -> Figure:
        if feature_id not in range(1, 4):
            return Figure()
        feature_name = f"feature_{feature_id}"
        feature_title = feature_name.replace('_', ' ').title()
        df = self.df()
        cross_tab = pd.crosstab(
            df["target"],
            df[feature_name],
        )
        data = [
            go.Bar(name=col, x=cross_tab.index, y=cross_tab[col])
            for col in cross_tab.columns
        ]
        title = f"Target by {feature_title} Crosstab"
        layout = go.Layout(
            title=title,
            barmode="stack",
            colorway=px.colors.qualitative.Antique,
        )
        return go.Figure(data=data, layout=layout)

    def target_percent_vis(self):
        df = self.df()["target"].value_counts().to_frame()
        data = go.Pie(
            labels=df.index.values,
            values=df["target"],
            textinfo='label+percent',
            showlegend=False,
            hole=0.5,
        )
        layout = go.Layout(
            title="Target Percentage",
            colorway=px.colors.qualitative.Antique,
        )
        return go.Figure(data=data, layout=layout)


if __name__ == '__main__':
    db = Data()
    # db._action("DROP TABLE features")
    # db._setup("features", [
    #     "idx SERIAL PRIMARY KEY NOT NULL",
    #     "feature_1 INT8 NOT NULL",
    #     "feature_2 INT8 NOT NULL",
    #     "feature_3 INT8 NOT NULL",
    #     "target varchar(10) NOT NULL"
    # ])
    # db.reset()
    # db.seed(1024)
    db.crosstab_vis(1).show()
    # db.target_percent_vis().show()
