import React from 'react';
import pets from '../images/pets.png';
import Container from '@material-ui/core/Container';
import {makeStyles} from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import CssBaseline from "@material-ui/core/CssBaseline";

const useStyles = makeStyles((theme) => ({
    heroContent: {
        padding: theme.spacing(8, 0, 6),
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

export default function About() {
    const classes = useStyles();
    return (
        <React.Fragment>
            <CssBaseline/>
            <Container maxWidth="sm" component="main" className={classes.heroContent}>
                <Typography component="h1" variant="h2" align="center" color="textPrimary" gutterBottom>
                    Welcome to PetClinic
                </Typography>
                <Typography variant="h5" align="center" color="textSecondary" component="p">
                    <img src={pets} alt="pets"/>
                </Typography>
            </Container>
        </React.Fragment>
    )
}