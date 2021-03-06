import React from "react";
import { Typography, Grid } from "@material-ui/core";

const Header = () => {
  return (
    <div className="Header">
      <Grid item xs={12} sm={6} style={{ margin: "auto" }}>
        <img src="/nemo.jpg" alt="nemo_logo" className="Logo" />
      </Grid>
      <Grid item xs={12} sm={6} >
        <Typography variant="h2" style={{fontWeight: "bold", textAlign: 'left' }}>
          SCIENCE LIVE
        </Typography>
        <Typography variant="h4" style={{fontWeight: "bold", textAlign: 'left' }}>
        Werk aan de wetenschap
        </Typography>
      </Grid>
      <Grid item xs={12} sm={6}>
        <br/>
        <br/>
        <Typography variant="h5" style={{ textAlign: 'left' }}>
        Toestemmingsformulier minderjarigen
        </Typography>
      </Grid>
    </div>
  );
};

export default Header;
