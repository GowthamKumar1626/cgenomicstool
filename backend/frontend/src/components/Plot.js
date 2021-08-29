import React from "react";
import moment from "moment";

import Timeline from "./Timeline";

function Plot() {
  let startDate = moment().add(-365, "days");
  let dateRange = [startDate, moment()];

  let data = Array.from(new Array(365)).map((_, index) => {
    return {
      date: moment(startDate).add(index, "day"),
      value: Math.floor(Math.random() * 100),
    };
  });

  return (
    <>
      <Timeline
        range={dateRange}
        data={data}
        colorFunc={({ alpha }) => `rgba(3, 160, 3, ${alpha})`}
      />
    </>
  );
}

export default Plot;
