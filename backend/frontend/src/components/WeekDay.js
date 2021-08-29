import React from "react";

function WeekDay({ index }) {
  const DayNames = {
    1: "Mon",
    3: "Wed",
    5: "Fri",
  };
  return <div className="timeline-weekdays-weekday">{DayNames[index]}</div>;
}

export default WeekDay;
