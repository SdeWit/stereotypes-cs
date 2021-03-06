import React from "react";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import CssBaseline from "@material-ui/core/CssBaseline";
import Container from "@material-ui/core/Container";
import useStyles from '../../styles/Information'
import Grid from "@material-ui/core/Grid";

const Information = (props) => {
  /*eslint-disable */
  const classes = useStyles();

  var playing = false;

  function audio_ended() {
    playing = false;
  };

  const playSound = audioFile => {
    if (playing===false){
      audioFile.play(); 
      playing = true;
      setTimeout(audio_ended, 15000)
    }
  }

  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="sm" component="main" className={classes.heroContent}>
        <Typography
          variant="h4"
          align="center"
          color="textSecondary"
          gutterBottom
        >
          {props.text}
        </Typography>
      </Container>

      <Grid container>
        <Grid item xs={6} sm={6}>
          <Button
            onClick={() => playSound(new Audio(props.audio))}
            variant="contained"
            style={{ marginTop: 20}}
            color="primary"
          > 
            Voorlezen
          </Button>
        </Grid>
          
        <Grid item xs={6} sm={6}>
          <Button
            variant="contained"
            style={{ marginTop: 20 }}
            color="primary"
            onClick={props.onNext}
          >
            VOLGENDE
          </Button>
        </Grid>
      </Grid>

    </React.Fragment>
  );
};

export default Information;
