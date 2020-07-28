import React from "react";
import { useState, useEffect } from "react";
import Button from "@material-ui/core/Button";
import { InputLabel } from "@material-ui/core";
import { getVersions } from "../utils/requests/getQuiz";
import { FormControl, MenuItem, Select } from "@material-ui/core";
import { makeStyles } from "@material-ui/core";
import { Grid } from "@material-ui/core";
import { Link } from "react-router-dom";

var modules = require("react-export-excel");

const useStyles = makeStyles((theme) => ({
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120,
  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
}));

const Load = (props) => {
  const classes = useStyles();

  const [state, setstate] = useState({ isLoading: false, version: props.version });
  const [checkedVersion, setversion] = useState(props.version);
  const [versions, setversions] = useState(false);


  useEffect(() => {
    if (props.loadFailed) setstate({ isLoading: false });
  }, [props.loadFailed]);

  useEffect(() => {
    if (props.isDataLoaded) {
      setstate({ isLoading: false });
    }
  }, [props.isDataLoaded]);

  useEffect(() => {
    if (!versions) {
      fetchVersions();
    }
  }, [versions]);

  // Get the versions of the quiz.
  // If any error occurs, always select the first version.
  const fetchVersions = async () => {
    getVersions()
      .then((res) => {
        setversions(res.data);
      })
      .catch(setversions({ A: "Version 1" }));
  };

  // Function to determine the version of the quiz to be loaded.
  // If the value string is 'R' the quiz is randomly selected.
  const getCurrentVersion = (version) => {
    var ver = version;
    if (version === "R"){
      ver = Object.keys(versions)[Math.floor(Math.random() * Object.keys(versions).length)];
    }
    return ver;
  };

  return (
    <div style={{ width: "50%", paddingTop: 200, margin: "auto" }}>
      <Grid container spacing={2}>
        {/* LOAD QUESTIONS BUTTON */}
        <Grid item xs={6} style={{ textAlign: "left", margin: "auto" }}>
          <Button
            style={{ margin: "auto" }}
            variant="contained"
            color="primary"
            disabled={checkedVersion === "" || state.isLoading}
            onClick={() => {
              setstate({ isLoading: true });
              props.onLoadData(getCurrentVersion(checkedVersion));
            }}
          >
            {" "}
            LOAD QUESTIONS{" "}
          </Button>
        </Grid>
      </Grid>
      {/* ERROR MESSAGE */}
      <InputLabel
        error
        style={{
          visibility: props.loadFailed ? "visible" : "hidden",
          marginTop: 20,
        }}
      >
        Data load failed
      </InputLabel>
      {/* START BUTTON */}
      <Link
        to={props.isDataLoaded ? "/app" : "/load"}
        style={{ textDecoration: "none" }}
      >
        <Button
          variant="contained"
          color="secondary"
          style={{ marginTop: 50 }}
          disabled={!props.isDataLoaded}
        >
          Start session
        </Button>
      </Link>
    </div>
  );
};

export default Load;
