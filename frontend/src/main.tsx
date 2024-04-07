import ReactDOM from 'react-dom/client';
import App from './components/App/App.tsx';
import './index.scss';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from './services/store.ts';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { CssBaseline } from '@mui/material';

const theme = createTheme({
  typography: {
    fontFamily: 'InterVariable, sans-serif',
  },
  palette: {
    primary: {
      main: '#1D4ED8',
    },
  },
  components: {
    MuiButton: {
      defaultProps: {
        disableRipple: true,
      },
      styleOverrides: {
        root: () => ({
          paddingBlock: '10px',
          width: '100%',
          borderRadius: '8px',
          boxShadow: 'none',
          fontSize: '16px',
          fontWeight: 400,
          textTransform: 'none',
          '&:active': {
            boxShadow: 'none',
            backgroundColor: '#1E40AF',
          },
          '&:hover': {
            boxShadow: 'none',
            backgroundColor: 'none',
          },
        }),
      },
    },
    MuiTab: {
      defaultProps: {
        disableRipple: true,
      },
      styleOverrides: {
        root: {
          textTransform: 'none',
          color: '#333333',
        },
      },
    },
    MuiTabs: {
      styleOverrides: {
        flexContainer: {
          justifyContent: 'flex-start',
          gap: '4px',
          containertype: 'inline-size',
          '& button': {
            minWidth: '0',
            flexGrow: 1,
            transition:
              'background-color 0.3s ease-in-out, color 0.3s ease-in-out',
            borderRadius: '12px',
            padding: '10px 12px',
            fontSize: '16px',
            fontWeight: 400,
            lineHeight: '1.5',
            minHeight: 'inherit',
          },
          '& button:active': { backgroundColor: '#1E40AF', color: '#FFFFFF' },
          '& button.Mui-selected': {
            backgroundColor: '#1D4ED8',
            color: '#FFFFFF',
          },
          '@media (max-width: 374px)': {
            '& button': {
              fontSize: '4.0cqw',
            },
          },
        },
      },
    },
    MuiAccordion: {
      styleOverrides: {
        root: () => ({
          borderRadius: '12px',
          boxShadow:
            '0 4px 90px 0 rgba(95, 105, 131, 0.16), 0 5px 4px 0 rgba(95, 105, 131, 0.08), 0 0 4px 0 rgba(95, 105, 131, 0.06)',
          '&.Mui-expanded': {
            margin: 0,
          },
          ':last-of-type': {
            borderRadius: '12px',
          },
          ':first-of-type': {
            borderRadius: '12px',
          },
          "&.MuiAccordion-root:before": {
            backgroundColor: "transparent"
        }
        }),
      },
    },
    MuiAccordionSummary: {
      styleOverrides: {
        root: () => ({
          margin: '0',
          paddingBlock: '16px 8px',
          paddingInline: '12px',
        }),
        content: () => ({
          margin: 0,
          paddingRight: '8px',
          '&.Mui-expanded': {
            margin: 0,
          },
        }),
      },
    },
  },
});

ReactDOM.createRoot(document.getElementById('root')!).render(
  // <React.StrictMode>
  <Provider store={store}>
    <CssBaseline>
      <ThemeProvider theme={theme}>
        <BrowserRouter basename={import.meta.env.BASE_URL}>
          <App />
        </BrowserRouter>
      </ThemeProvider>
    </CssBaseline>
  </Provider>
  // </React.StrictMode>
);
