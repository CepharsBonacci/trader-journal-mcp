import pandas as pd

from sqlalchemy.orm import sessionmaker

from app.database import engine
from app.models import Trade

Session = sessionmaker(bind=engine)


def import_trades(csv_path):

    df = pd.read_csv(csv_path)

    session = Session()

    imported = 0
    skipped = 0

    for _, row in df.iterrows():

        existing_trade = (
            session.query(Trade)
            .filter_by(ticket=int(row["ticket"]))
            .first()
        )

        if existing_trade:
            skipped += 1
            continue

        trade = Trade(
            ticket=int(row["ticket"]),
            symbol=row["symbol"],
            direction=row["direction"],
            open_time=row["open_time"],
            close_time=row["close_time"],
            volume=float(row["volume"]),
            open_price=float(row["open_price"]),
            close_price=float(row["close_price"]),
            profit=float(row["profit"]),
            commission=float(row["commission"]),
            swap=float(row["swap"])
        )

        session.add(trade)
        imported += 1

    session.commit()
    session.close()

    print(
        f"Imported: {imported} | Skipped duplicates: {skipped}"
    )