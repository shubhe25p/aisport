import Webcam from "react-webcam";
import ReactPlayer from "react-player";
import Grid from "@mui/material/Grid";

export default function WebCamVideo(){
    return (
        <Grid sx={{flexGrow: 1}} container spacing={1}>
            <Grid item xs={6}>
                <Grid container justifyContent="center" spacing={2}>
                <Webcam />
                </Grid>
            
            </Grid>
            <Grid item xs={6}>
            <Grid container justifyContent="center" spacing={2}>
            <ReactPlayer url="https://www.youtube.com/shorts/VvWL2Y5M_hk" width='1000px' height='480px' playing muted/>
            </Grid>
           
            </Grid>
        </Grid>
    );
}