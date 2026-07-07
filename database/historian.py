import sqlite3
from datetime import datetime


class Historian:

    def __init__(self):

        self.connection = sqlite3.connect("factory.db")

        self.cursor = self.connection.cursor()
    
    def total_events(self):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM machine_events
            """
        )

        return self.cursor.fetchone()[0]
    
    def alarms(self):

        self.cursor.execute(
            """
            SELECT *
            FROM machine_events
            WHERE event_type='ALARM_TRIGGERED'
            """
        )

        return self.cursor.fetchall()

    def log_event(
        self,
        machine,
        event_type,
        details
    ):

        self.cursor.execute(
            """
            INSERT INTO machine_events
            (
                timestamp,
                machine,
                event_type,
                details
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                datetime.now(),
                machine,
                event_type,
                str(details)
            )
        )

         # Save structured data
        if event_type == "UNIT_PROCESSED":
            self.log_production(machine, details)

        elif event_type == "OEE_UPDATED":
            self.log_oee(machine, details)

        elif event_type == "ALARM_TRIGGERED":
            self.log_alarm(machine, details)

        if event_type in (
            "STATE_CHANGED",
            "UNIT_PROCESSED",
            "OEE_UPDATED",
            "ALARM_TRIGGERED"
        ):
            self.update_machine_status(machine, event_type, details)

        self.connection.commit()
    
    def log_production(self, machine, details):

        self.cursor.execute(
            """
            INSERT INTO production_history
            (
                timestamp,
                machine,
                lot_id,
                units_processed,
                good_units,
                bad_units,
                yield_rate,
                cycle_time
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.now(),
                machine,
                details.get("lot_id", "UNKNOWN"),
                details.get("units_processed", 0),
                details.get("good_units", 0),
                details.get("bad_units", 0),
                details.get("yield_rate", 0),
                details.get("cycle_time", 0)
            )
    )
        
    def log_oee(self, machine, details):

        self.cursor.execute(
            """
            INSERT INTO oee_history
            (
                timestamp,
                machine,
                availability,
                performance,
                quality,
                oee
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.now(),
                machine,
                details.get("availability", 0),
                details.get("performance", 0),
                details.get("quality", 0),
                details.get("oee", 0)
            )
    )

    def log_alarm(self, machine, details):

        self.cursor.execute(
            """
            INSERT INTO alarm_history
            (
                timestamp,
                machine,
                alarm_code,
                description
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                datetime.now(),
                machine,
                details.get("alarm", ""),
                details.get("alarm", "")
            )
    )

    def update_machine_status(
    self,
    machine,
    event_type,
    details
    ):

        self.cursor.execute(
            """
            INSERT OR REPLACE INTO machine_status
            (
                machine,
                state,
                lot_id,
                units_processed,
                good_units,
                bad_units,
                current_oee,
                availability,
                performance,
                quality,
                current_alarm,
                last_updated
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                machine,
                details.get("state", ""),
                details.get("lot_id", ""),
                details.get("units_processed", 0),
                details.get("good_units", 0),
                details.get("bad_units", 0),
                details.get("oee", 0),
                details.get("availability", 0),
                details.get("performance", 0),
                details.get("quality", 0),
                details.get("alarm", ""),
                datetime.now()
            )
    )  

