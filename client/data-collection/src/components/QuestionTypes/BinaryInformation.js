import React, { useState } from "react";
import UIFx from 'uifx';
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import CssBaseline from "@material-ui/core/CssBaseline";
import Container from "@material-ui/core/Container";
import { makeStyles } from "@material-ui/core";
import GridListTile from "@material-ui/core/GridListTile";
import GridList from "@material-ui/core/GridList";

const useStyles = makeStyles((theme) => ({
  "@global": {
    ul: {
      margin: 0,
      padding: 0,
      listStyle: "none",
    },
  },
  appBar: {
    borderBottom: `1px solid ${theme.palette.divider}`,
  },
  toolbar: {
    flexWrap: "wrap",
  },
  toolbarTitle: {
    flexGrow: 1,
  },
  link: {
    margin: theme.spacing(1, 1.5),
  },
  heroContent: {},
  cardHeader: {
    backgroundColor:
      theme.palette.type === "light"
        ? theme.palette.grey[200]
        : theme.palette.grey[700],
  },
  cardPricing: {
    display: "flex",
    justifyContent: "center",
    alignItems: "baseline",
    marginBottom: theme.spacing(2),
  },
  footer: {
    borderTop: `1px solid ${theme.palette.divider}`,
    marginTop: theme.spacing(8),
    paddingTop: theme.spacing(3),
    paddingBottom: theme.spacing(3),
    [theme.breakpoints.up("sm")]: {
      paddingTop: theme.spacing(6),
      paddingBottom: theme.spacing(6),
    },
  },
  gridList: {
    paddingTop: 25,
  },
}));

const Information = (props) => {
  /*eslint-disable */
  const classes = useStyles();

  const [hasNext, sethasNext] = useState(false);
  const [startsIn, setStartIn] = useState(false);

  const likeAudio = new Audio('https://res.cloudinary.com/hwutobbxz/video/upload/v1596200543/audio/intro_hgujds.m4a');

  const playSound = audioFile => {
    audioFile.play();
}

  return (
    <React.Fragment>
      <CssBaseline />
      {startsIn ? (
        <div style={{marginTop: '30%'}}>
        <Typography
          variant="h1"
          align="center"
          color="textPrimary"
        >
          {startsIn}
        </Typography>
        </div>
      ) : (
        <React.Fragment>

          <Button
              onClick={() => playSound(likeAudio)}
              variant="contained"
              color="primary"
          > Geluid
          </Button>

          <Typography
            variant="h5"
            align="center"
            color="textPrimary"
            component="p"
          >
            {props.text0}
          </Typography>

          <Container maxWidth component="main" className={classes.heroContent}>
            <div style={{ paddingTop: 30 }}>
              <Typography
                variant="h5"
                align="center"
                color="textSecondary"
                component="p"
              >
                {props.text1}
              </Typography>
            </div>
            <GridList
              cellHeight="auto"
              className={classes.gridList}
              cols={props.images0.length}
            >
              {props.images0.map((image) => (
                <GridListTile style={props.images0.length === 4 ? {width: '19%', margin:'auto'} : {}} key={image} cols={1}>
                  <img
                    style={{ width: "100%", height: "auto" }}
                    src={image}
                    alt={image}
                  />
                </GridListTile>
              ))}
            </GridList>
            <div style={{ paddingTop: 25 }}>
              <Typography
                variant="h5"
                align="center"
                color="textSecondary"
                component="p"
              >
                {props.text2}
              </Typography>
            </div>
            <GridList
              cellHeight="auto"
              className={classes.gridList}
              cols={props.images1.length}
            >
              {props.images1.map((image) => (
                <GridListTile style={props.images0.length === 4 ? {width: '19%', margin:'auto'} : {}} key={image} cols={1}>
                  <img
                    style={{ width: "100%", height: "auto" }}
                    src={image}
                    alt={image}
                  />
                </GridListTile>
              ))}
            </GridList>
            <div style={{ paddingTop: 25 }}>
              <Typography
                variant="h5"
                align="center"
                color="textPrimary"
                component="p"
              >
                {props.text3}
              </Typography>
            </div>
          </Container>
          <Button
            variant="contained"
            style={{ marginTop: 20 }}
            onClick={() => {
              sethasNext(true);
              setTimeout(props.onNext, 4000);
              setStartIn(3);
              setTimeout(() => setStartIn(2), 1000);
              setTimeout(() => setStartIn(1), 2000);
              setTimeout(() => setStartIn("Start!"), 3000);
            }}
            disabled={hasNext}
          >
            Volgende
          </Button>
        </React.Fragment>
      )}
    </React.Fragment>
  );
};

export default Information;
