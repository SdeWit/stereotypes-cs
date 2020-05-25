export const saveQuestionAction = (data, questionType, time=0) => {
  return {
    type: "SAVE_QUESTION_ANSWER",
    data: data,
    questionType: questionType,
  };
};

export const clearQuestionsStore = () => {
    return {
        type: "CLEAR_QUESTIONS"
    }
}

export const sendQuestionsAnswers = () => {
  return {
    type: "SEND_QUESTIONS_ANSWERS"
  }
}