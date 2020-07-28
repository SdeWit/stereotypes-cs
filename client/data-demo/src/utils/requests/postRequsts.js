import axios from "../API";

/*
Check credentials and request Authorization
*/
export function login(data, callback, errorcallback) {
  axios
    .post("/login", data)
    .then((res) => {
      if (callback != null && res.status === 200) {
        callback(res);
      }
    })
    .catch((err) => {
      if (errorcallback != null) {
        errorcallback(err);
      }
    });
}
