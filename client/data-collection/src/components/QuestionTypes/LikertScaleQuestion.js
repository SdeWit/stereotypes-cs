import '../../styles/Question.css';
import React, { useState } from 'react';
import Likert from 'react-likert-scale';
import { likertScaleText } from '../../utils/constants/LikertScale';
import { saveQuestionAction } from '../../actions/question';
import { connect } from 'react-redux';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import CardHeader from '@material-ui/core/CardHeader';
import CssBaseline from '@material-ui/core/CssBaseline';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles((theme) => ({
  '@global': {
    ul: {
      margin: 0,
      padding: 0,
      listStyle: 'none',
    },
  },
  appBar: {
    borderBottom: `1px solid ${theme.palette.divider}`,
  },
  toolbar: {
    flexWrap: 'wrap',
  },
  toolbarTitle: {
    flexGrow: 1,
  },
  link: {
    margin: theme.spacing(1, 1.5),
  },
  heroContent: {
    padding: theme.spacing(6, 0, 6),
  },
  cardHeader: {
    backgroundColor:
      theme.palette.type === 'light'
        ? theme.palette.grey[200]
        : theme.palette.grey[700],
  },
  cardPricing: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'baseline',
    marginBottom: theme.spacing(2),
  },
  footer: {
    borderTop: `1px solid ${theme.palette.divider}`,
    marginTop: theme.spacing(8),
    paddingTop: theme.spacing(3),
    paddingBottom: theme.spacing(3),
    [theme.breakpoints.up('sm')]: {
      paddingTop: theme.spacing(6),
      paddingBottom: theme.spacing(6),
    },
  },
}));


const giveMeString = function(index, id) {
  // Jongens - Meisjes
  //  12
  if(id == 12){
    if(index == '1')
      return "Jongens"
    else if(index == '2')
      return "Een beetje meer voor jongens";
    else if(index == '3')
      return "Allebei";
    else if(index == '4')
      return "Een beetje meer voor meisjes";
    else if(index == '5')
      return "Meisjes";
    return index.toString();
  }
    

  // Programmeur - Schrijver
  // 6 - 10
  else if(id >= 5 && id <= 10){
    if(index == '1')
      return "Programmeur"
    else if(index == '2')
      return "Een beetje meer een programmeur";
    else if(index == '3')
      return "Allebei";
    else if(index == '4')
      return "Een beetje meer een schrijver";
    else if(index == '5')
      return "Schrijver";
    return index.toString();
  }

  // Helemaal mee eens - helemaal mee oneens
  // 1 - 5, 10 11 13 14 
  // default

  else {
    if(index == '1')
      return "Helemaal eens"
    else if(index == '2')
      return "Een beetje eens";
    else if(index == '3')
      return "Neutraal";
    else if(index == '4')
      return "Een beetje oneens";
    else if(index == '5')
      return "Helemaal oneens";
    return index.toString();
  }

}

const LikertScaleQuestion = (props) => {
  const classes = useStyles();
  const [state, setQuestionAnswer] = useState({ answers: [] });
  const onClick = () => {
    props.submitSelectedScale(state);
    props.onNext();
    setQuestionAnswer({ answers: [] });
  };

  const likertOptions = {
    responses: likertScaleText.map((scaleText, index) => {
      return { value: index + 1, text: giveMeString(scaleText, props.id) };
    }),
    picked: (val) => {
      setQuestionAnswer({ answers: parseInt(val), question_id: props.id });
    },
  };

  var playing = false;

  function audio_ended() {
    playing = false;
  };

  const playSound = audioFile => {
    if (playing==false){
      audioFile.play(); 
      playing = true;
      setTimeout(audio_ended, 5000)
    }
  }

  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth='sm' component='main' className={classes.heroContent}>
        <Typography
          component='p'
          variant='h4'
          align='center'
          color='textPrimary'
          gutterBottom
        >
          {props.text}
        </Typography>
      </Container>
      <Container maxWidth='md' component='main'>
        <Grid container spacing={5} alignItems='flex-end'>
          <Grid item xs={12} md={12} style={{ margin: 'auto' }}>
            <Card>
              <CardHeader
                title='Wat vind jij?'
                titleTypographyProps={{ align: 'center', variant: 'h6' }}
                subheaderTypographyProps={{ align: 'center' }}
                action={null}
                className={classes.cardHeader}
              />
              <CardContent>
                <Likert
                  key={props.questionIndex}
                  {...likertOptions}
                  className='likertScale'
                />
              </CardContent>
            </Card>
           
            <Grid container>
              <Grid item xs={6}>
                <Button
                    onClick={() => playSound(new Audio(props.audio))}
                    variant="contained"
                    color="primary"
                    style={{ marginTop: '20px' }}
                > Voorlezen
                </Button>
              </Grid>

              <Grid item xs={6}>
                <Button
                  style={{ marginTop: '20px' }}
                  color="primary"
                  className={classes.nextButton}
                  variant='contained'
                  disabled={state.answers.length === 0 && !playing}
                  onClick={onClick}
                >
                  VOLGENDE
                </Button>
              </Grid>
            </Grid>
            
          </Grid>
        </Grid>
      </Container>
    </React.Fragment>
  );
};

const mapStateToProps = (state, ownProps) => {
  return {
    ...ownProps,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    submitSelectedScale: (answer) => {
      dispatch(saveQuestionAction(answer));
    },
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(LikertScaleQuestion);
