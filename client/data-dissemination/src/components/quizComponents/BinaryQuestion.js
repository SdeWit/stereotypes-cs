import React, { useState, useEffect } from "react";
import { Grid, Typography } from "@material-ui/core";
import ImageCard from "./ImageCard";
import ChoiceCard from "./ChoiceCard";
import { useStyles } from "../../styles/BinaryQuestion";

const BinaryQuestion = (props) => {
  const classes = useStyles();
  const [start, setstart] = useState(Date.now);
  const [wrong, setwrong] = useState(0);
  const [imageLoaded, setimageLoaded] = useState(false);

  //on mount reset answer variables
  useEffect(() => {
    setstart(Date.now());
    setwrong(0);
    setimageLoaded(false);
  }, []);

  // save answer to store
  const sumbitAnswerToStore = () => {
    const time = Date.now() - start;
    const answer = {
      response_time: time,
      answers: wrong,
      question_id: props.id,
      img_id: props.image.link,
      block_nr: props.block_nr
    };
    props.registerAnswer(answer);
    setTimeout(props.onNext, 200);
  };

  // handle click on left pad
  const onClickLeft = () => {
    if (props.categories_left.map(category => category.name).indexOf(props.image.category) > -1) {
      sumbitAnswerToStore();
    } else {
      setwrong(wrong + 1);
    }
  };

  // handle click on right pad
  const onClickRight = () => {
    if (props.categories_right.map(category => category.name).indexOf(props.image.category) > -1) {
      sumbitAnswerToStore();
    } else {
      setwrong(wrong + 1);
    }
  };

  return (
    <div className={classes.root}>
      <Grid container spacing={0}>
        {/* left text */}
        <Grid className={classes.paper} item xs={4}>
          {props.categories_left.map(category => (
            <Typography variant="h6">{category.name}</Typography>
          ))}
        </Grid>
        {/* X */}
        <Grid item xs={4}>
          <Typography
            variant="h3"
            align="center"
            style={{ visibility: wrong ? "visible" : "hidden", color: "red" }}
          >
            X
          </Typography>
        </Grid>
        {/* right text */}
        <Grid className={classes.paper} item xs={4}>
        {props.categories_right.map(category => (
            <Typography variant="h6">{category.name}</Typography>
          ))}
        </Grid>
        {/* choice card left */}
        <Grid xs={12} style={{ marginTop: "3em" }} />
        <ChoiceCard onClick={onClickLeft} imageLoaded={imageLoaded} />
        <Grid item xs={4}>
          {/* image card */}
          <ImageCard
            key={props.image.link}
            image={props.image.link}
            onImageLoaded={() => {
              setimageLoaded(true);
              setstart(Date.now());
            }}
            imageLoaded={imageLoaded}
          />
        </Grid>
        {/* choice card right */}
        <ChoiceCard onClick={onClickRight} imageLoaded={imageLoaded} />
      </Grid>
    </div>
  );
};

export default BinaryQuestion;
