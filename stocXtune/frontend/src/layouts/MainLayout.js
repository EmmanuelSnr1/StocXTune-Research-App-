import {Outlet} from 'react-router-dom'
import {Header} from "../components/Header";
import {ErrorBoundary} from "../components/ErrorBoundary";
import {Footer} from "../components/Footer";
import {LoadingIndicator} from "../components/LoadingIndicator";

export default function MainLayout() {

    return (
        <>
            <Header/>
            <ErrorBoundary>
                <Outlet/>
            </ErrorBoundary>
            <Footer/>
        </>
    );
}

