import {makeStyles} from "@material-ui/core/styles";

export const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        width: '95%',
        marginTop: '10%',
        margin: 'auto',
    },
    image: {
        height: '100%',
        width:'100%',
        transform: 'scale(1.05)',
    },
    imageFocus: {
        transition: 'transform .2s',
    },
}));