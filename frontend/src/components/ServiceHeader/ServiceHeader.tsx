import styled from 'styled-components';
import { IServiceExtended } from '../../utils/interfaces/interfaces';

interface IServiceHeaderProps {
  selectSubscription: IServiceExtended;
  className?: string;
}

const HeaderWrapper = styled.div`
  display: flex;
  justify-content: flex-start;
  align-items: center;
  gap: 16px;

  & h2 {
    margin: 0;
  }

  & img {
    max-height: 56px;
    border-radius: 50px;
  }
`;

function ServiceHeader(props: IServiceHeaderProps) {
  return (
    <HeaderWrapper className={props.className}>
      <img src={props.selectSubscription.icon_small} alt="" />
      <h2>{props.selectSubscription.name}</h2>
    </HeaderWrapper>
  );
}

export default ServiceHeader;
