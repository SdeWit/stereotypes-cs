const initialStore = {
  appReducer: {
    quizIndex: 0,
    quizData: [
      { type: 1, correctAnswer: "right" },
      { type: 1, correctAnswer: "right" },
    ],
    quizIsLoaded: true,
    quizIsLoading: true,
    quizIsFinished: false,
  },
};
export default initialStore;
