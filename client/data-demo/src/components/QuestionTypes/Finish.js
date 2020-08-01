import React, { useState, useEffect } from "react";
import {
  clearQuestionsStore,
  sendQuestionsAnswers,
} from "../../actions/question";
import { connect } from "react-redux";
import Button from "@material-ui/core/Button";
import {
  Typography,
  Grid,
} from "@material-ui/core";
import CssBaseline from "@material-ui/core/CssBaseline";
import Container from "@material-ui/core/Container";
import useStyles from "../../styles/Finish";


const Finish = (props) => {
  const classes = useStyles();

  const [finish, setfinish] = useState(true);

  const onCheck = (event) => {
    setfinish(!event.target.checked);
  };

  const onClick = () => {
     props.clearQuestionsStore();
     props.onFinish();
  };

  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="sm" component="main" className={classes.heroContent}>
        <Typography
          component="h1"
          variant="h1"
          align="center"
          color="textPrimary"
          gutterBottom
        >
          {props.title}
        </Typography>
        <Typography
          variant="h5"
          align="center"
          color="textSecondary"
          component="p"
        >
          {props.text}
        </Typography>
      </Container>
      <Grid>
        <Button
          style={{ marginTop: 20 }}
          variant="contained"
          onClick={onClick}
        >
          EINDE
        </Button>
      </Grid>
    </React.Fragment>
  );
};

const mapStateToProps = (state, ownProps) => {
  return {
    ...ownProps,
    sendDataStatus: state.mainAppReducer.sendDataStatus,
    childId: state.mainAppReducer.activeChild.id,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    sendQuestionsAnswers: (childId) => dispatch(sendQuestionsAnswers(childId, '', dispatch)),
    clearQuestionsStore: () => dispatch(clearQuestionsStore()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Finish);
