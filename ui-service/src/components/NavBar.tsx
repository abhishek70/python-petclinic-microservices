import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';
import {makeStyles} from '@material-ui/core/styles';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link as RouterLink
} from 'react-router-dom';
import SignIn from './SignIn';
import SignUp from './SignUp';
import About from './About';

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
}));

const routes = [
    {
        path: "/",
        exact: true,
        component: About
    },
    {
        path: "/auth/signin",
        component: SignIn
    },
    {
        path: "/auth/signup",
        component: SignUp
    }
];

function RouteWithSubRoutes(route: any) {
    return (
        <Route
            path={route.path}
            render={props => (
                // pass the sub-routes down to keep nesting
                <route.component {...props} routes={route.routes}/>
            )}
        />
    );
}

export default function NavBar() {
    const classes = useStyles();

    return (
        <React.Fragment>
            <Router>
                <CssBaseline/>
                <AppBar position="static" color="default" elevation={0} className={classes.appBar}>
                    <Toolbar className={classes.toolbar}>
                        <Typography variant="h6" color="inherit" noWrap className={classes.toolbarTitle}>
                            PetClinic
                        </Typography>
                        <Button href="/auth/signin" color="primary" variant="outlined" className={classes.link}>
                            Sign In
                        </Button>
                        <Button href="/auth/signup" color="primary" variant="contained" className={classes.link}>
                            Sign Up
                        </Button>
                    </Toolbar>
                </AppBar>
                <Switch>
                    {routes.map((route, i) => (
                        <RouteWithSubRoutes key={i} {...route} />
                    ))}
                </Switch>
            </Router>
        </React.Fragment>
    );
}