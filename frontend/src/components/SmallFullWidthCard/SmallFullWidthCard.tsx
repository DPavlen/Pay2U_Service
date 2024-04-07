import styled from 'styled-components';

interface ISmallFullWidthCardProps {
  card: {
    name: string;
    icon: string | {};
  };
  description?: string;
}

const Card = styled.div`
  container-type: inline-size;
  font-size: 14px;
  font-weight: 600;
  line-height: 1.43;
  box-sizing: border-box;
  padding: 12px 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  border-radius: 12px;
  box-shadow: 0 4px 15px 0 rgba(95, 105, 131, 0.12),
    0 5px 4px 0 rgba(95, 105, 131, 0.05), 0 0 4px 0 rgba(95, 105, 131, 0.07);
  color: var(--black);

  & img {
    width: 24px;
    height: 24px;
  }
  
  & h3 {
    font-size: inherit;
    font-weight: inherit;
    margin: 0;

    @media (max-width: 374px) {
      font-size: 4.3cqw;
    }
  }
  & p {
    margin: 0;
  }
`;

const TitleWrapper = styled.div`
  display: flex;
  align-items: center;
  gap: 6px;
`;
export default function SmallFullWidthCard(props: ISmallFullWidthCardProps) {
  return (
    <Card>
      <TitleWrapper>
        <img src={props.card.icon as string} alt="" />
        <h3>{props.card.name}</h3>
      </TitleWrapper>
      <p>{props.description}</p>
    </Card>
  );
}
