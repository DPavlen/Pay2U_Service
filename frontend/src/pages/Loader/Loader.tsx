import { CircularProgress } from '@mui/material';
import './Loader.scss';
import styled from 'styled-components';

const LoaderWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100svh - 52px);
`;

export default function () {
  return (
    <LoaderWrapper>
      <CircularProgress size={90} />
    </LoaderWrapper>
  );
}
