import React, { Component } from "react";
import Grid from "@material-ui/core/Grid";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import Signature from "react-signature-canvas";
import Button from "@material-ui/core/Button";
import "./style/Form.css";
import Child from "./ChildField";
import Parent from "./ParentField";
import Email from "./EmailField";
import Loader from "../../common/Loader";
import InputLabel from "@material-ui/core/InputLabel";
import validator from "validator";
const max_no_children = process.env.REACT_APP_NO_CHILD;

class Footer extends Component {
  constructor(props) {
    super(props);
    this.signatureDiv = { width: 300, height: 100 };
    this.emailRef = React.createRef();
    this.props = props;

    this.state = {
      isMailInvalid: false,
      isSigned: false,
      hasValidFields: false,
      isSubmittable: false,
      isAgreed: false,
      signature: null,
      children: [{ firstName: "", lastName: "", isValid: false }],
      parent: { firstName: "", lastName: "", isValid: false },
      email: "",
    };
  }

  onSubmit = () => {
    if (
      validator.isEmail(this.emailRef.current.value) ||
      this.emailRef.current.value === ""
    ) {
      const dataToSend = { ...this.state, email: this.emailRef.current.value };
      this.props.onSubmit(dataToSend)();
    } else {
      this.setState({ ...this.state, isMailInvalid: true });
      setTimeout(
        () => this.setState({ ...this.state, isMailInvalid: false }),
        2000
      );
    }
  };
  componentDidMount = () => {
    this.signatureRef.off();
    this.signatureRef.getCanvas().width = document
      .getElementById("signature")
      .getBoundingClientRect().width;
    this.signatureRef.getCanvas().height = document
      .getElementById("signature")
      .getBoundingClientRect().height;
  };

  componentDidUpdate(prevProps) {
    console.log(max_no_children);
    if (!this.state.isSigned && !this.signatureRef.isEmpty()) {
      this.setState({ isSigned: true });
    }
    var isSubmittableNow = true;
    isSubmittableNow =
      this.state.hasValidFields && this.state.isSigned && this.state.isAgreed;

    var hasValidFieldsNow = true;
    hasValidFieldsNow &= this.state.parent.isValid;
    this.state.children.forEach((element) => {
      hasValidFieldsNow &= element.isValid;
    });

    if (isSubmittableNow !== this.state.isSubmittable) {
      this.setState({ isSubmittable: isSubmittableNow });
    }

    if (hasValidFieldsNow !== this.state.hasValidFields) {
      this.setState({ hasValidFields: hasValidFieldsNow });
    }
  }

  onAddClick = () => {
    var newChild = { firstName: "", lastName: "", isValid: false };
    this.setState({
      children: [...this.state.children, newChild],
      hasValidFields: false,
    });
  };

  onRemoveClick = () => {
    var newChildren = this.state.children;
    newChildren.pop();
    this.setState({
      children: newChildren,
    });
  };
  agreedChanged = (event) => {
    if (this.state.isAgreed) {
      this.signatureRef.clear();
      this.signatureRef.off();
      this.setState({ isSubmittable: false, isAgreed: false, isSigned: false });
    } else {
      this.signatureRef.on();
      this.setState({ isAgreed: true });
    }
  };

  render() {
    var parent = this.state.parent;
    return (
      <div className="Footer">
        <Grid container spacing={3} className="TextFields" justify="center">
          <Parent
            firstName={parent.firstName}
            lastName={parent.lastName}
            component={this}
          />
          {this.state.children.map((child, index) => {
            return (
              <Child
                firstName={child.firstName}
                lastName={child.lastName}
                id={index}
                key={index}
                component={this}
              />
            );
          })}
          <Email ref={this.emailRef} />
        </Grid>
        <InputLabel style={{marginTop: 10, visibility: this.state.isMailInvalid ? 'visible' : 'hidden'}} error={true}> Ongeldig e-mail </InputLabel>
        <div className="PlusMinusButton">
          {this.state.children.length > max_no_children ? null : (
            <div className="Button">
              <Button
                size="small"
                variant="contained"
                color="primary"
                disableElevation
                onClick={this.onAddClick}
              >
                +
              </Button>
            </div>
          )}
          {this.state.children.length === 1 ? null : (
            <div className="Button">
              <Button
                className="Button"
                size="small"
                variant="contained"
                color="primary"
                disableElevation
                onClick={this.onRemoveClick}
              >
                -
              </Button>
            </div>
          )}
        </div>
        <Grid item xs={12} style={{ marginTop: "20px" }}>
          <FormControlLabel
            control={
              <Checkbox
                onClick={this.agreedChanged}
                color="secondary"
                name="agree"
                value="yes"
              />
            }
            label="Ga akkoord om gegevens te delen en te ondertekenen*"
          />
        </Grid>
        <Grid item xs={12}>
          <div className="Signature" id="signature">
            <Signature
              ref={(ref) => {
                this.signatureRef = ref;
              }}
              canvasProps={{
                width: this.signatureDiv.width,
                height: this.signatureDiv.height,
              }}
              onEnd={() =>
                this.setState({
                  isSigned: true,
                  signature: this.signatureRef
                    .getTrimmedCanvas()
                    .toDataURL("image/png"),
                })
              }
            ></Signature>
          </div>
        </Grid>
        {this.props.isLoading ? (
          <Loader />
        ) : (
          <Button
            variant="contained"
            color="primary"
            size="large"
            disableElevation={true}
            disabled={!this.state.isSubmittable}
            onClick={this.onSubmit}
          >
            Verzenden
          </Button>
        )}
      </div>
    );
  }
}

export default Footer;
