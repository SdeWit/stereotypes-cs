
const questionsReducer = (
  state = { answers: [], before_video: true, participant_id: undefined, version: 'R' },
  action
) => {
  switch (action.type) {

    case 'SET_VERSION':
      return {
        ...state,
        version: action.version
      }

    /*
    Save question answer in store
    */
    case 'SAVE_QUESTION_ANSWER':
      const newAnswer = {
        ...action.data,
        before_video: state.before_video,
        participant_id: state.participant_id,
        questionType: action.questionType,
      };
      const newAnswers = [...state.answers, newAnswer];
      return {
        ...state,
        answers: newAnswers,
      };

    /*
    Clear question results from store
    */
    case 'CLEAR_QUESTIONS':
      return { ...state, before_video: true, participant_id: undefined, answers: [] };

    case 'VIDEO_WAS_PLAYED':
      return {
        ...state,
        before_video: false,
      };

    default:
      return state;
  }
};

export default questionsReducer;
